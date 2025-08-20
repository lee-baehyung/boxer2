import string
import uuid
from typing import ClassVar

# from typing_extensions import Final


class Base62:
    BASE: ClassVar[str] = string.ascii_letters + string.digits
    BASE_LEN: ClassVar[int] = len(BASE)
    print(BASE_LEN)

    # def __init__(self, base: str):
    #     self.BASE = base

    @classmethod
    def encode(cls, num: int) -> str:
        if num < 0:
            raise ValueError(f"{cls}.encode() needs positive integer but you passed: {num}")

        if num == 0:
            return cls.BASE[0]

        result = []
        # result = ""
        while num:
            num, remainder = divmod(num, cls.BASE_LEN)
            result.append(cls.BASE[remainder])
            # result += cls.BASE[remainder]
        return "".join(result)


# print(uuid.uuid4().int)
uu = 314931652839392640128428240003443324402
print(Base62.encode(uu))
# print(Base62.encode(uuid.uuid4().int))
# print(Base62.encode(124))
# print(Base62.encode(2))
