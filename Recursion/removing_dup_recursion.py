def remove_dup(nums):
    
    if len(nums) <= 1:
        return nums
    
    rest = remove_dup(nums[1:])

    if nums[0] not in rest:

        return [nums[0]] + rest
    
    else:
        return rest
    
nums = [2,4,5,7,8,2,4,3,4,5,6]
res = remove_dup(nums)
print(res)