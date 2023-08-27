import sys


def binary_search(tails, key, length):
    left, right = 0, length - 1
    while left <= right:
        mid = left + (right - left) // 2
        if tails[mid] >= key:
            left = mid + 1
        else:
            right = mid - 1
    return left


# trying to make an algorithm O(nlog(n))
def lds_bu_faster(n: int, arr: list):
    tails = [0] * n  # Массив для отслеживания "хвостов" последовательностей
    tails[0] = arr[0]
    lds_indexes = [0] * n  # Массив для индексов предыдущих элементов
    length = 1

    for i in range(1, n):
        if arr[i] > tails[0]:
            tails[0] = arr[i]
            lds_indexes[i] = 0
        elif arr[i] <= tails[length - 1]:
            tails[length] = arr[i]
            lds_indexes[i] = length
            length += 1
        else:
            pos = binary_search(tails, arr[i], length)
            tails[pos] = arr[i]
            lds_indexes[i] = pos

    lds_sequence_indexes = [-1] * length
    current_length = length - 1
    for i in range(n - 1, -1, -1):
        if lds_indexes[i] == current_length:
            lds_sequence_indexes[current_length] = i + 1
            current_length -= 1

    return length, lds_sequence_indexes


# O(n**2)
def lds_bu(n: int, seq: list) -> tuple:
    d = list()
    prev = list()
    for i in range(n):
        d.append(1)
        prev.append(-1)
        for j in range(i):
            if seq[i] <= seq[j] and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
                prev[i] = j

    ans = max(d)
    k = d.index(ans)
    lds_indexes = [0 for _ in range(ans)]

    j = ans-1
    while k >= 0:
        lds_indexes[j] = k + 1
        j = j-1
        k = prev[k]

    return ans, lds_indexes


def read_input():
    n = int(sys.stdin.readline())
    seq = list(map(int, sys.stdin.readline().split()))
    return n, seq
    # return 5, [5, 3, 4, 4, 2]


def main():
    k, indexes = lds_bu_faster(*read_input())
    print(k)
    print(*indexes)


def test():
    assert lds_bu_faster(5, [5, 3, 4, 4, 2]) == (4, [1, 3, 4, 5])                               # test 1
    assert lds_bu_faster(1, [1]) == (1, [1])                                                    # test 2
    assert lds_bu_faster(2, [1, 2]) == (1, [2])                                                 # test 3
    assert lds_bu_faster(2, [2, 1]) == (2, [1, 2])                                              # test 4
    assert lds_bu_faster(2, [1, 1]) == (2, [1, 2])                                              # test 5
    assert lds_bu_faster(10, [9, 10, 6, 3, 6, 8, 7, 9, 6, 5]) == (5, [2, 6, 7, 9, 10])          # test 6
    assert lds_bu_faster(10, [2, 3, 1, 2, 1, 3, 2, 1, 1, 2]) == (5, [2, 6, 7, 8, 9])             # test 7
    assert lds_bu_faster(100, [64, 80, 90, 69, 23, 78, 30, 76, 11, 2, 7, 42, 13, 45,
                               40, 52, 31, 42, 33, 74, 37, 64, 2, 26, 88, 51, 53, 95,
                               26, 7, 58, 9, 30, 29, 53, 69, 3, 71, 40, 89, 32, 90,
                               14, 49, 18, 70, 37, 79, 6, 48, 25, 28, 7, 81, 35, 99,
                               1, 1, 28, 17, 56, 77, 11, 64, 28, 6, 9, 62, 32, 2, 31,
                               29, 23, 50, 89, 95, 54, 36, 13, 52, 77, 58, 80, 58, 21,
                               20, 1, 82, 27, 31, 84, 14, 73, 55, 2, 69, 95, 33, 70, 72]) \
           == (18, [3, 6, 8, 20, 22, 31, 35, 44, 50, 55, 69, 71, 72, 73, 85, 86, 92, 95])       # test 8


if __name__ == "__main__":
    # test()
    main()
