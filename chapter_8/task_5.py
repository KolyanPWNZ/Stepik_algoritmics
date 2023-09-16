import sys


def ladder_td(n: int, step_score: int) -> int:


    return 1




def read_data():
    n = int(sys.stdin.readline())
    steps_score = map(int, sys.stdin.readline().split())
    return n, steps_score


def main():
    print(ladder_td(*read_data()))


if __name__ == "__main__":
    main()