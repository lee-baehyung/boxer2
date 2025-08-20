from app.dtos.frozen_config import FROZEN_CONFIG
from typing import Annotated
from pydantic import BaseModel, Field


class CreateMeetingResponse(BaseModel):
    model_config = FROZEN_CONFIG

    url_code: Annotated[str, Field(description="미팅 url 코드. unique 합니다.")]
