def bubble_sort(nums):
    for i in range(len(nums) - 1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j + 1]:
                temp = nums[j]
                nums[j] = nums[j + 1]
                nums[j + 1] = temp
    return nums


numbers = [-4, -7, 8, 9, 2, 1, 65, -2, 0, 14]

print(bubble_sort(numbers))
print('Hello')
