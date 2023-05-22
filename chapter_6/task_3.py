

def read_points():
    return list(map(int, input().split()))


def read_segments(n: int) -> list:
    return [list(map(int, input().split())) for _ in range(n)]


def read_data() -> tuple:
    n, m = map(int, input().split())
    return read_segments(n), read_points()


def swap_el(A, i, j):
    A[i], A[j] = A[j], A[i]


def partition(array_part, column_index) -> int:
    l = 0
    pivot = array_part[l][column_index]
    j = l
    for i in range(1, len(array_part)):
        if array_part[i][column_index] <= pivot:
            j = j + 1
            swap_el(array_part, i, j)

    swap_el(array_part, l, j)
    return j


def quick_sort_2d_array(array: list, column_index: int = 0) -> list:
    n = len(array)
    if n <= 1:
        return array

    m = partition(array, column_index)
    left_part = quick_sort_2d_array(array[:m], column_index)
    right_part = quick_sort_2d_array(array[m+1:], column_index)
    return left_part + [array[m]] + right_part


def points_and_segments(segments: list, points: list):
    quick_sort_2d_array(segments)
    for point in points:
        counter_entry = 0
        for segment in segments:
            if segment[0] <= point <= segment[1]:
                counter_entry = counter_entry + 1
        print(counter_entry, end=" ")


def test():
    array_src_1 = [[3, 4], [6, 3], [2, 3], [5, 3], [1, 5], [4, 6]]
    array_dst_1 = [[1, 5], [2, 3], [3, 4], [4, 6], [5, 3], [6, 3]]
    assert quick_sort_2d_array(array_src_1) == array_dst_1, "test№1 - failed: non-correct quick sort"

    # segments = [[0, 3], [1, 3], [2, 3], [3, 4], [3, 5], [3, 6]]
    # points = [1, 2, 3, 4, 5, 6]
    # assert points_and_segments(segments, points)


def main():
    segments, points = read_data()
    points_and_segments(segments, points)


if __name__ == "__main__":
    test()
    main()