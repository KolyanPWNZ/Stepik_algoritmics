import sys

def binary_search(tails, key):
    left, right = 0, len(tails) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if tails[mid] > key:
            left = mid + 1
        else:
            right = mid - 1
    return left


# trying to make an algorithm O(nlog(n))
def lds_bu_faster(n: int, arr: list):
    n = len(arr)
    tails = [0] * n  # Массив для отслеживания "хвостов" последовательностей
    lds_indexes = [-1] * n  # Массив индексов ННП (наиб. невоз. последов.)
    tails[0] = arr[0]
    lds_indexes[0] = 1
    length = 1

    for i in range(1, n):
        if arr[i] >= tails[0]:
            tails[0] = arr[i]
            lds_indexes[0] = i + 1
        elif arr[i] <= tails[length - 1]:
            tails[length] = arr[i]
            lds_indexes[length] = i + 1
            length += 1
        else:
            pos = binary_search(tails[:length], arr[i])
            tails[pos] = arr[i]
            lds_indexes[pos] = i + 1

    return length, lds_indexes[:length]


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


if __name__ == "__main__":
    main()
