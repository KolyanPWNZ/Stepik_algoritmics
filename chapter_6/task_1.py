from math import floor


def read_sequency():
    n, *A = map(int, input().split())
    return A, n


def binary_search(array: list, size_array: int, number: int) -> int:
    """
    :param array: input array
    :param size_array:  size of input array
    :param number:  desired number
    :return: index of desired number in array or -1
    """
    l = 0
    r = size_array - 1
    while l <= r:
        m = floor(l + (r - l)/2)
        if array[m] == number:
            return m
        elif array[m] < number:
            l = m + 1
        else:
            r = m - 1

    return -1


def main():
    a, n = read_sequency()
    b, k = read_sequency()

    for i in b:
        index = binary_search(a, n, i) + 1
        if index:
            print(index, end = " ")
        else:
            print(-1, end=" ")


if __name__ == "__main__":
    main()
