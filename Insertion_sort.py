def insertion_sort(nums:list[int]):
    l = len(nums)
    for i in range(1, l):
        current = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > current:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j+1] = current
    return nums

print(insertion_sort([3, 5, 4, 1, 2]))