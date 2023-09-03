import sys


def diff(symb1: str, symb2: str) -> int:
    return int(symb1 != symb2)


def edit_dist_bu(arr_src: str, arr_dst: str) -> int:
    n = len(arr_src)
    m = len(arr_dst)
    d = [[0] * (m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        d[i][0] = i
    for j in range(1, m+1):
        d[0][j] = j

    for i in range(1, n+1):
        for j in range(1, m+1):
            c = diff(arr_src[i-1], arr_dst[j-1])
            d[i][j] = min(d[i-1][j] + 1,
                          d[i][j-1] + 1,
                          d[i-1][j-1] + c)
    return d[n][m]


def read_data():
    return sys.stdin.readline().replace('\n', ''), sys.stdin.readline().replace('\n', '')


def main():
    print(edit_dist_bu(*read_data()))


if __name__ == "__main__":
    main()
