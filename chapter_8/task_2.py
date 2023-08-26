import sys


def read_input():
    n = int(sys.stdin.readline())
    seq = list(map(int, sys.stdin.readline().split()))
    return n, seq


def main():
    n, seq = read_input()


if __name__ == "__main__":
    main()
