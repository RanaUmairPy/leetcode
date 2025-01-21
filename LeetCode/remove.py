def fun(nums, val):
    index = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[index] = nums[i]
            index += 1
    return nums[:index]
     

nums = [3, 2, 2, 3, 5, 7, 8]
val = 3
print(fun(nums, val))
