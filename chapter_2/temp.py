def find_max(nums):
    max_num = float("-inf")
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


nums = [1, 2, 4, 22, 123, 132, 54]
print(find_max(nums))