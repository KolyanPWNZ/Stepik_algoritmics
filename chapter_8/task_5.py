import sys


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


def read_data():
    n = int(sys.stdin.readline())
    steps_score = list(map(int, sys.stdin.readline().split()))
    return n, steps_score


def test():
    assert -63 == ladder_td(5, [-2, -16, -13, -9, -48]), "test 1  is failed"
    assert 2 == ladder_td(7, [1, 1, -2, -4, -6, 2, 2]), "test 2  is failed"
    assert -73 == ladder_td(5, [-64, -16, -13, -9, -48]), "test 3  is failed"
    assert 5 == ladder_td(6, [0, 0, 0, 4, 6, -5]), "test 4  is failed"
    assert -9 == ladder_td(6, [-6, 4, -16, -13, -9, 0],), "test 5  is failed"
    assert -18 == ladder_td(5, [-6, 4, -16, -13, -9]), "test 6  is failed"
    assert 21 == ladder_td(8, [3, 4, 10, 10, 0, -6, -10, 0]), "test 7  is failed"
    assert 3 == ladder_td(2, [1, 2]), "test 8  is failed"
    assert 1 == ladder_td(2, [2, -1]), "test 9  is failed"
    assert 3 == ladder_td(3, [-1, 2, 1]), "test 10  is failed"
    assert 2 == ladder_td(1, [2]), "test 11  is failed"
    assert -2 == ladder_td(1, [-2]), "test 12  is failed"
    print ("testing is finished")



def main():
    print(ladder_td(*read_data()))


if __name__ == "__main__":
    # test()
    main()