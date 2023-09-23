import sys
from enum import Enum
from collections import deque


class Method(Enum):
    BOTTOM_UP = 1
    DEQUE = 2


def specific_calculator_deque(n):
    visited = [False] * (n + 1)
    parent = [None] * (n + 1)
    operations = [None] * (n + 1)

    queue = deque()
    queue.append(1)
    visited[1] = True

    while queue:
        current = queue.popleft()

        if current == n:
            break

        operations_list = [current * 2, current * 3, current + 1]

        for op_index, op in enumerate(operations_list):
            if op <= n and not visited[op]:
                visited[op] = True
                parent[op] = current
                operations[op] = op_index
                queue.append(op)

    k = 0
    sequence = [n]
    while n != 1:
        operation_index = operations[n]
        if operation_index == 0:
            n = n // 2
        elif operation_index == 1:
            n = n // 3
        else:
            n = n - 1
        sequence.append(n)
        k += 1

    sequence.reverse()
    return k, *sequence


def specific_calculator_bu(b) -> tuple:
    return 1


def specific_calculator(n: int, method: Method = Method.BOTTOM_UP) -> tuple:
    result = 0
    if method == Method.BOTTOM_UP:
        result = specific_calculator_bu(n)
    elif method == Method.DEQUE:
        result = specific_calculator_deque(n)
    else:
        raise ValueError("The wrong method is selected")

    return result


def read_data() -> int:
    return int(sys.stdin.readline())


def test(method: Method = Method.BOTTOM_UP):
    tests = [
        {
            "in": 10,
            "out": (3, 1, 3, 9, 10)
        },
        {
            "in": 1,
            "out": (0, 1)
        },
        {
            "in": 5,
            "out": (3, 1, 2, 4, 5)
        },
        {
            "in": 96234,
            "out": (14, 1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038, 16039, 32078, 96234)
        }
    ]
    for index, test_current in enumerate(tests):
        result = specific_calculator(test_current["in"], method)
        assert test_current["out"] == result, f"test №{index+1} is failed, a value {test_current['out']} was expected," \
                                              f"and {result} was received"


def main(method: Method = Method.BOTTOM_UP):
    specific_calculator(read_data(), method)


if __name__ == "__main__":
    test(method=Method.DEQUE)
    # main(method=Method.TOP_DOWN)
