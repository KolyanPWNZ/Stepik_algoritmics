import sys
from enum import Enum


class Method(Enum):
    TO_DOWN = 1
    BOTTOM_UP = 2
    BOTTOM_UP_OPTIMIZE = 3


def ladder_td(i, s: list, D: list = list(), low_limit: int = 10**(-5)) -> int:
    if not len(D):
        D = [low_limit for _ in range(i+1)]

    if D[i] == low_limit:
        if i == 0:
            D[i] = 0
        elif i == 1:
            D[i] = s[i-1]
        else:
            D[i] = s[i-1] + max(ladder_td(i-1, s, D),
                                ladder_td(i-2, s, D))
    return D[i]


def ladder_bu(n: int, s: list) -> int:
    D = [0 for _ in range(n+1)]
    D[0] = 0
    D[1] = s[0]
    for i in range(2, n+1):
        D[i] = s[i-1] + max(D[i-1], D[i-2])
    return D[n]


def ladder_bu_optim(n: int, s: list) -> int:
    if len(s) == 1:
        return s[0]
    prev_1 = 0
    prev_2 = s[0]
    for i in range(2, n+1):
        current = s[i-1] + max(prev_1, prev_2)
        prev_1 = prev_2
        prev_2 = current
    return current


def ladder(n: int, s: list,  D: list = list(), low_limit: int = 10**(-5), method: Method = Method.TO_DOWN) -> int:
    result = 0
    if method == Method.TO_DOWN:
        result = ladder_td(n, s, D, low_limit)
    elif method == Method.BOTTOM_UP:
        result = ladder_bu(n, s)
    else:
        result = ladder_bu_optim(n, s)
    return result


def read_data():
    n = int(sys.stdin.readline())
    steps_score = list(map(int, sys.stdin.readline().split()))
    return n, steps_score


def test(method: Method = Method.TO_DOWN):
    assert -63 == ladder(5, [-2, -16, -13, -9, -48], method=method), "test 1  is failed"
    assert 2 == ladder(7, [1, 1, -2, -4, -6, 2, 2], method=method), "test 2  is failed"
    assert -73 == ladder(5, [-64, -16, -13, -9, -48], method=method), "test 3  is failed"
    assert 5 == ladder(6, [0, 0, 0, 4, 6, -5], method=method), "test 4  is failed"
    assert -9 == ladder(6, [-6, 4, -16, -13, -9, 0], method=method), "test 5  is failed"
    assert -18 == ladder(5, [-6, 4, -16, -13, -9], method=method), "test 6  is failed"
    assert 21 == ladder(8, [3, 4, 10, 10, 0, -6, -10, 0], method=method), "test 7  is failed"
    assert 3 == ladder(2, [1, 2], method=method), "test 8  is failed"
    assert 1 == ladder(2, [2, -1], method=method), "test 9  is failed"
    assert 3 == ladder(3, [-1, 2, 1], method=method), "test 10  is failed"
    assert 2 == ladder(1, [2], method=method), "test 11  is failed"
    assert -2 == ladder(1, [-2], method=method), "test 12  is failed"
    print ("testing is finished")


def main(method: Method = Method.TO_DOWN):
    print(ladder(*read_data(), method=method))


if __name__ == "__main__":
    # test(method=Method.BOTTOM_UP_OPTIMIZE)
    main(method=Method.BOTTOM_UP_OPTIMIZE)