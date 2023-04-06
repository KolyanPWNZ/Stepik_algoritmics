

def merge(left_part: list, right_part: list) -> tuple:
    comb_data = []
    num_rec = 0
    while len(left_part):
        if left_part[0] <= right_part[0]:
            comb_data.append(left_part.pop(0))
        else:
            comb_data.append(right_part.pop(0))

    if len(left_part):
        comb_data.extend(left_part)
    elif len(right_part):
        comb_data.extend(right_part)

    return comb_data, num_rec


def merge_sorting(src_array: list) -> tuple:
    queue_proc = []
    num_rec = 0
    for el in src_array:
        queue_proc.append([el])

    while len(queue_proc) > 1:
        queue_proc.append(merge(queue_proc.pop(0),
                                queue_proc.pop(0)))
    return queue_proc, num_rec


def main():
    n = int(input())
    array = list(map(int, input().split()))
    array_sort, num_rec = merge_sorting(array)
    print(array_sort)
    print(num_rec)


if __name__ == "__main__":
    main()
