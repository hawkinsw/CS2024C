from typing import Generator, TypeVar

T = TypeVar("T")
def take(value: int, g: Generator[T, None, None]) -> Generator[T, None, None]:
    for i in range(0, value):
        yield next(g)


def infin() -> Generator[int, None, None]:
    value = 0
    while True:
        yield value
        value += 1

def infis() -> Generator[str, None, None]:
    value = ""
    while True:
        yield value
        value += ";"


take_ten_pauses = take(10, infis())
take_five = take(5, take_ten_pauses)
result = list(take_five)
print(f"{result=}")

take_ten = take(10, infin())
take_five = take(5, take_ten)
result = list(take_five)
print(f"{result=}")

for i in take(5, infin()):
    print(f"{i=}")