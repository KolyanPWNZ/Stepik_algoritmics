import sys
from enum import Enum


class Method(Enum):
    TO_DOWN = 1
    BOTTOM_UP = 2


def specific_calculator_td(n: int):
    return 1


def specific_calculator_bu() -> tuple:
    return 1


def specific_calculator(n: int, method: Method = Method.BOTTOM_UP) -> tuple :
    if method == Method.BOTTOM_UP:
        specific_calculator_bu(n)
    else:
        specific_calculator_bu(n)


def read_data() -> int:
    return int(sys.stdin.readline())


def main(method: Method = Method.BOTTOM_UP):
    specific_calculator(read_data(), method)


if __name__ == "__main__":
    main()