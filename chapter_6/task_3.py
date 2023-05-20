

def read_points():
    return list(map(int, input().split()))


def read_segments(n: int) -> list:
    return [list(map(int, input().split())) for _ in range(n)]


def read_data() -> tuple:
    n, m = map(int, input().split())
    return read_segments(n), read_points()


def swap_el(A, i, j):
    A[i], A[j] = A[j], A[i]


def partition(array_part) -> int:
    pivot = array_part[0]
    j = 0
    for i in range(1, len(array_part)):
        if array_part[i] <= pivot:
            swap_el(array_part, i, j)
            j = j + 1
    # swap_el(array_part, i, j)
    return j


def quick_sort(array: list):
    n = len(array)
    if n == 1:
        return

    m = partition(array)
    quick_sort(array[0:m+1])
    quick_sort(array[m+1:])


def points_and_segments(segments: list, points: list):
    quick_sort(points)
    for point in points:
        counter_entry = 0
        for segment in segments:
            if segment[0] <= point <= segment[1]:
                counter_entry = counter_entry + 1
        print(counter_entry, end=" ")


def main():
    segments, points = read_data()
    # segments = [[0, 3], [1, 3], [2, 3], [3, 4], [3, 5], [3, 6]]
    # points = [1, 2, 3, 4, 5, 6]
    points_and_segments(segments, points)





if __name__ == "__main__":
    main()