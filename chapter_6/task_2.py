import time
import random
import cProfile


def merge(left_part: list, right_part: list) -> tuple:
    comb_data = []
    num_inv = 0
    indx_left = 0
    indx_right = 0
    len_left_part = len(left_part)
    len_right_part = len(right_part)

    while indx_left < len_left_part and indx_right < len_right_part:
        if left_part[indx_left] <= right_part[indx_right]:
            comb_data.append(left_part[indx_left])
            indx_left += 1
        else:
            comb_data.append(right_part[indx_right])
            num_inv += len_left_part - indx_left
            indx_right += 1

    if indx_left < len(left_part):
        comb_data += left_part[indx_left:]
    elif indx_right < len(right_part):
        comb_data += right_part[indx_right:]

    return comb_data, num_inv


def merge_sorting_iterative(src_array: list) -> tuple:
    queue_proc = []
    num_inv = 0
    for el in src_array:
        queue_proc.append([el])

    while len(queue_proc) > 1:
        sub_array, num_inv_cur = merge(queue_proc.pop(0), queue_proc.pop(0))
        queue_proc.insert(0, sub_array)
        num_inv += num_inv_cur
    return queue_proc.pop(0), num_inv


def merge_sorting_recursive(src_array: list) -> tuple:
    n = len(src_array)
    if n == 1:
        return src_array, 0
    else:
        mid = n // 2
        left_part, num_inv_left = merge_sorting_recursive(src_array[:mid])
        right_part, num_inv_right = merge_sorting_recursive(src_array[mid:])
        merged_array, num_inv_merged = merge(left_part, right_part)
        return  merged_array, num_inv_merged + num_inv_left + num_inv_right



def generate_input_array(size_array: int, max_value: int = 10**9) -> list:
    return [random.randint(0, max_value) for _ in range(size_array)]


def test():
    array_test = generate_input_array(1000)
    num_tests = 10
    total_time = 0
    for i in range(num_tests):
        start_time = time.time()
        array_sort, num_inv = merge_sorting_recursive(array_test)
        end_time = time.time()
        total_time += end_time - start_time
    avg_time = total_time / num_tests
    print("Среднее ремя выполнение программы: {:.5f} секунд".format(avg_time))


def main():
    n = int(input())
    array = list(map(int, input().split()))
    array_sort, num_inv = merge_sorting_recursive(array)
    # print(array_sort)
    print(num_inv)


if __name__ == "__main__":
    # cProfile.run('test()')
    # test()
    main()

