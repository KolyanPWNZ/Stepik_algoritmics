import sys


def lisd_bu(n: int, seq: list) -> int:
    d = list([1 for _ in range(n)])
    for i in range(n):
        for j in range(i):
            if seq[i] % seq[j] == 0 and d[j] + 1 > d[i]:
                d[i] = d[j] + 1
    return max(d)


def read_input():
    n = int(sys.stdin.readline())
    seq = list(map(int, sys.stdin.readline().split()))
    return n, seq


def main():
    print(lisd_bu(*read_input()))


if __name__ == "__main__":
    main()

# 4
# 3 6 7 12