import sys


def knapsack_bu(capacity: int, n: int, w: list) -> int:
    return 1


def read_data():
    capacity, n = map(int, sys.stdin.readline().split())
    w = list(map(int, sys.stdin.readline().split()))
    return capacity, n, w


def main():
    knapsack_bu(*read_data())


if __name__ == "__main__":
    main()