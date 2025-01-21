def fun(nums):
    
    
    i = 0
    while i < len(nums): 
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                nums.pop(j)
                break
        else:
            i += 1
    return nums

nums = [1,1,0,0,0,3, 2, 2, 3, 5, 7, 8]
print(fun(nums))