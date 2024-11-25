def sum_even(nums):
    if nums == []:
        return 0
    if nums[0] % 2 != 0:
        return sum_even(nums[1:])
    else:
        return nums[0] + sum_even(nums[1:])
    
lst = [6,7,2,3,8,9]
res = sum_even(lst)
print(res)