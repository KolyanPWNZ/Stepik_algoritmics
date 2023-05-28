import copy
import random
import time
import cProfile


def read_points():
    return list(map(int, input().split()))


def read_segments(n: int) -> list:
    return [list(map(int, input().split())) for _ in range(n)]


def read_data() -> tuple:
    n, m = map(int, input().split())
    return read_segments(n), read_points()


def partition(array_part, column_index, lb, rb) -> int:
    mid = (lb + rb) // 2
    if array_part[mid][column_index] < array_part[lb][column_index]:
        array_part[lb], array_part[mid] = array_part[mid], array_part[lb]
    if array_part[rb][column_index] < array_part[lb][column_index]:
        array_part[lb], array_part[rb] = array_part[rb], array_part[lb]
    if array_part[rb][column_index] < array_part[mid][column_index]:
        array_part[rb], array_part[mid] = array_part[mid], array_part[rb]

    pivot = array_part[lb][column_index]
    j = lb
    for i in range(lb+1, rb+1):
        if array_part[i][column_index] < pivot:
            j = j + 1
            array_part[i], array_part[j] = array_part[j], array_part[i]

    array_part[lb], array_part[j] = array_part[j], array_part[lb]
    return j


def quick_sort_2d_array(array: list, column_index: int = 0, lb: int = 0, rb: int = 0):
    stack = [(lb, rb)]
    while stack:
        lb, rb = stack.pop()
        if lb >= rb:
            continue

        m = partition(array, column_index, lb, rb)
        stack.append((lb, m - 1))
        stack.append((m + 1, rb))


def left_border_search(segments: list, point: int) -> int:
    low = 0
    high = len(segments)
    while low < high:
        mid = (low + high) // 2
        if segments[mid][0] <= point:
            low = mid + 1
        else:
            high = mid
    return low


def right_border_search(segments: list, point: int) -> int:
    low = 0
    high = len(segments)
    while low < high:
        mid = (low + high) // 2
        if segments[mid][1] < point:
            low = mid + 1
        else:
            high = mid
    return low


def points_and_segments(segments: list, points: list) -> list:
    segments_sort_by_left_side = copy.copy(segments)
    segments_sort_by_right_side = copy.copy(segments)

    quick_sort_2d_array(segments_sort_by_left_side, 0, 0, len(segments)-1)
    quick_sort_2d_array(segments_sort_by_right_side, 1, 0, len(segments)-1)

    result_intersection = list()
    for point in points:
        n = left_border_search(segments_sort_by_left_side, point)
        m = right_border_search(segments_sort_by_right_side, point)
        result_intersection.append(n-m)
    return result_intersection


def generate_input_data(num_segments: int, num_points: int, limit_coordinate_size = 100000000) -> tuple:
    segments = list()
    for _ in range(num_segments):
        lb = random.randint(0, limit_coordinate_size-1)
        rb = random.randint(lb+1, limit_coordinate_size)
        segments.append([lb, rb])
    points = [random.randint(0, limit_coordinate_size) for _ in range (num_points)]

    return segments, points


def test():
    print("test №1")
    array_src_1 = [[3, 4], [6, 3], [2, 3], [5, 3], [1, 5], [4, 6]]
    array_dst_1 = [[1, 5], [2, 3], [3, 4], [4, 6], [5, 3], [6, 3]]
    quick_sort_2d_array(array_src_1, 0, 0, len(array_src_1)-1)
    assert array_src_1 == array_dst_1, f"test №1 - failed: non-correct quick sort - {array_src_1}"

    print("test №2")
    segments = [[0, 3], [3, 4], [1, 3], [2, 3], [3, 5], [3, 6]]
    points = [1, 2, 3, 4, 5, 6]
    result = points_and_segments(segments, points)
    result_target = [2, 3, 6, 3, 2, 1]
    assert result == result_target, "test №2 - failed: non-correct result of algorithm"

    print("test №3")
    segments, points = generate_input_data(5000, 1000)
    num_tests = 10
    total_time = 0
    profiler = cProfile.Profile()
    profiler.enable()
    for _ in range(num_tests):
        start_time = time.time()
        print(*points_and_segments(segments, points))
        total_time += time.time() - start_time
    avg_time = total_time / num_tests

    profiler.disable()
    profiler.print_stats()
    print("Average program execution time: {:.5f} sec".format(avg_time))


def main():
    segments, points = read_data()
    print(*points_and_segments(segments, points))


if __name__ == "__main__":
    # cProfile.run('test()')
    test()
    # main()