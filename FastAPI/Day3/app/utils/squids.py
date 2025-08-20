import uuid
import random
import timeit
from datetime import datetime
from typing import Sequence
from app.utils.base62 import Base62


from sqids import sqids

squid = sqids.Sqids()


class Squids:

    # @classmethod
    # def encode(cls, nums: list[int]) -> str:
    #     return squid.encode(nums)

    @classmethod
    def encode(cls, nums: Sequence[int]) -> str:
        return squid.encode(nums)

# print(Squids.encode([1, 2]))

# print(Squids.encode([uuid.uuid4().int]))

def do_squids():
    now = datetime.now()
    return Squids.encode(
        [now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, random.randint(1,9)]
    )

def do_base62():
    uu = uuid.uuid4()
    return Base62.encode(uu. int)

if __name__ == '__main__':
    print(timeit.timeit(lambda: do_squids(), number=100000))
    print(timeit.timeit(lambda: do_base62(), number=100000))
    # now = datetime.now()
    # Squids.encode(
    #         [now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond, random.randint(a:1, b:9)]
    # )


