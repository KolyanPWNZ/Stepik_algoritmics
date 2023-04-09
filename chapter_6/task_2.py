import time
import random


def merge(left_part: list, right_part: list) -> tuple:
    comb_data = []
    num_inv = 0
    indx_left = 0
    len_left_part_start = len(left_part)

    while len(left_part) and len(right_part):
        if left_part[0] <= right_part[0]:
            comb_data.append(left_part.pop(0))
            indx_left += 1
        else:
            comb_data.append(right_part.pop(0))
            num_inv += len_left_part_start - indx_left

    if len(left_part):
        comb_data += left_part
    elif len(right_part):
        comb_data += right_part

    return comb_data, num_inv


def merge_sorting(src_array: list) -> tuple:
    queue_proc = []
    num_inv = 0
    for el in src_array:
        queue_proc.append([el])

    while len(queue_proc) > 1:
        sub_array, num_inv_cur = merge(queue_proc.pop(0), queue_proc.pop(0))
        queue_proc.insert(0, sub_array)
        num_inv += num_inv_cur
    return queue_proc.pop(0), num_inv


def generate_input_array(size_array: int, max_value: int = 10**9) -> list:
    return [random.randint(0, max_value) for _ in range(size_array)]


def test():
    array_test = generate_input_array(1000)
    num_tests = 10
    total_time = 0
    for i in range(num_tests):
        start_time = time.time()
        array_sort, num_inv = merge_sorting(array_test)
        end_time = time.time()
        total_time += end_time - start_time
    avg_time = total_time / num_tests
    print("Среднее ремя выполнение программы: {:.5f} секунд".format(avg_time))


def main():
    n = int(input())
    array = list(map(int, input().split()))
    array_sort, num_inv = merge_sorting(array)
    # print(array_sort)
    print(num_inv)


if __name__ == "__main__":
    test()
    # main()