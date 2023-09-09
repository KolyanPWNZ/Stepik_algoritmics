import sys


def knapsack_bu(capacity: int, n: int, W: list) -> int:
    d = [[0] * (capacity+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, capacity+1):
            d[i][w] = d[i-1][w]
            if W[i-1] <= w:
                d[i][w] = max(d[i][w],
                               d[i-1][w-W[i-1]] + W[i-1])
    return d[n][capacity]


def read_data():
    capacity, n = map(int, sys.stdin.readline().split())
    w = list(map(int, sys.stdin.readline().split()))
    return capacity, n, w


def main():
    print(knapsack_bu(*read_data()))


if __name__ == "__main__":
    main()