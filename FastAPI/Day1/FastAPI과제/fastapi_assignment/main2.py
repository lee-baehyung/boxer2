from typing import Generator, Optional

from fastapi import FastAPI, HTTPException, Path, Query, Depends
from pydantic import BaseModel, Field
from enum import Enum
from sqlalchemy import Column, Integer, String, Enum as SqlEnum, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Session


DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    pass


class GenderEnum(str, Enum):
    male = "male"
    female = "female"



class UserCreateRequest(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., ge=0, le=120)
    gender: GenderEnum


class UserUpdateRequest(BaseModel):
    username: Optional[str] = Field(None, min_length=1, max_length=50)
    age: Optional[int] = Field(None, ge=0, le=120)


class UserQueryParams(BaseModel):
    username: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., gt=0, description="0보다 큰 값만 허용")
    gender: GenderEnum


class UserResponse(BaseModel):
    id: int
    username: str
    age: int
    gender: GenderEnum



class UserModel(Base):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username: str = Column(String(50), nullable=False)
    age: int = Column(Integer, nullable=False)
    gender: GenderEnum = Column(SqlEnum(GenderEnum), nullable=False)

    @classmethod
    def create(cls, db: Session, **kwargs: object) -> "UserModel":
        user = cls(**kwargs)  # type: ignore[arg-type]
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @classmethod
    def all(cls, db: Session) -> list["UserModel"]:
        return db.query(cls).all()

    def delete(self, db: Session) -> None:
        db.delete(self)
        db.commit()


Base.metadata.create_all(bind=engine)



app = FastAPI()



def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/users", response_model=UserResponse)
async def create_user(data: UserCreateRequest, db: Session = Depends(get_db)) -> UserResponse:
    user = UserModel.create(db, **data.model_dump())
    return UserResponse.model_validate(user)


@app.get("/users", response_model=list[UserResponse])
async def get_all_users(db: Session = Depends(get_db)) -> list[UserResponse]:
    users = UserModel.all(db)
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return [UserResponse.model_validate(u) for u in users]


@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int = Path(..., ge=1, description="조회할 유저의 ID (양수)"),
    db: Session = Depends(get_db)
) -> UserResponse:
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)


@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(
    user_id: int = Path(..., ge=1, description="업데이트할 유저의 ID (양수)"),
    data: Optional[UserUpdateRequest] = None,
    db: Session = Depends(get_db)
) -> UserResponse:
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if data:
        if data.username is not None:
            user.username = data.username
        if data.age is not None:
            user.age = data.age

    db.commit()
    db.refresh(user)
    return UserResponse.model_validate(user)


@app.delete("/users/{user_id}")
async def delete_user(
    user_id: int = Path(..., ge=1, description="삭제할 유저의 ID (양수)"),
    db: Session = Depends(get_db)
) -> dict[str, str]:
    user = db.query(UserModel).filter(UserModel.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.delete(db)
    return {"detail": f"User: {user_id}, Successfully Deleted."}


@app.get("/users/search", response_model=list[UserResponse])
async def search_users(
    params: UserQueryParams = Depends(),
    db: Session = Depends(get_db)
) -> list[UserResponse]:
    users = db.query(UserModel).filter_by(
        username=params.username,
        age=params.age,
        gender=params.gender
    ).all()

    if not users:
        raise HTTPException(status_code=404, detail="No matching users found")

    return [UserResponse.model_validate(u) for u in users]

