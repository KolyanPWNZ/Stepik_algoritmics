
def count_sort(array_a: list):
    n = len(array_a)
    m = max(array_a)
    array_b = [0 for _ in range(m+1)]
    array_a_new = [0 for _ in range(n)]

    for el in array_a:
        array_b[el] = array_b[el] + 1

    for i in range(1, len(array_b)):
        array_b[i] = array_b[i] + array_b[i-1]

    for i in range(n-1, -1, -1):
        array_a_new[array_b[array_a[i]]-1] = array_a[i]
        array_b[array_a[i]] = array_b[array_a[i]] - 1

    return array_a_new


def read_data():
    return int(input()), list(map(int, input().split()))


def main():
    _, array = read_data()
    print(*count_sort(array))


if __name__ == "__main__":
    main()