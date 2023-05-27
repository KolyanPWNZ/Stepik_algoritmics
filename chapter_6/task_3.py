import random
import time


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
    pivot_index = random.randint(0, len(array_part)-1)
    l = 0
    swap_el(array_part, pivot_index, l)
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


def left_border_search(segments: list, point: int) -> int:
    counter_entry = 0
    for segment in segments:
        if segment[0] > point:
            break
        counter_entry = counter_entry + 1
    return counter_entry


def right_border_search(segments: list, point: int) -> int:
    counter_entry = 0
    for segment in segments:
        if segment[1] >= point:
            break
        counter_entry = counter_entry + 1
    return counter_entry


def points_and_segments(segments: list, points: list) -> list:
    segments_sort_by_left_side = quick_sort_2d_array(segments, 0)
    segments_sort_by_right_side = quick_sort_2d_array(segments, 1)

    result_intersection = list()
    for point in points:
        n = left_border_search(segments_sort_by_left_side, point)
        m = right_border_search(segments_sort_by_right_side, point)
        result_intersection.append(n-m)
    return result_intersection


def print_result(results: list):
    for r in results:
        print(r, end=" ")


def generate_input_data(num_segments: int, num_points: int, limit_coordinate_size = 100000000) -> tuple:
    segments = list()
    for _ in range(num_segments):
        lb = random.randint(0, limit_coordinate_size-1)
        rb = random.randint(lb+1, limit_coordinate_size)
        segments.append([lb, rb])
    points = [random.randint(0, limit_coordinate_size) for _ in range (num_points)]

    return segments, points


def test():
    array_src_1 = [[3, 4], [6, 3], [2, 3], [5, 3], [1, 5], [4, 6]]
    array_dst_1 = [[1, 5], [2, 3], [3, 4], [4, 6], [5, 3], [6, 3]]
    assert quick_sort_2d_array(array_src_1) == array_dst_1, "test №1 - failed: non-correct quick sort"

    segments = [[0, 3], [1, 3], [2, 3], [3, 4], [3, 5], [3, 6]]
    points = [1, 2, 3, 4, 5, 6]
    result = points_and_segments(segments, points)
    result_target = [2, 3, 6, 3, 2, 1]
    assert result == result_target, "test №2 - failed: non-correct result of algorithm"

    segments, points = generate_input_data(5000, 1000)
    num_tests = 10
    total_time = 0
    for _ in range(num_tests):
        start_time = time.time()
        print(*points_and_segments(segments, points))
        total_time += time.time() - start_time
    avg_time = total_time / num_tests
    print("Average program execution time: {:.5f} sec".format(avg_time))



def main():
    segments, points = read_data()
    print(*points_and_segments(segments, points))


if __name__ == "__main__":
    test()
    # main()