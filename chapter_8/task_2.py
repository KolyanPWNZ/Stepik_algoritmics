import sys

# 5
# 5 3 4 4 2


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


def main():
    k, indexes = lds_bu(*read_input())
    print(k)
    print(*indexes)


if __name__ == "__main__":
    main()
