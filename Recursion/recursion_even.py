
def remove_even(nums):
    if nums == []:
        return [] # In the case when the list become empty, we should return a empty list

    if nums[0] % 2 == 0:
        return remove_even(nums[1:]) # Recursive call to remove the even value from nums by passing the nums by slicing after the occurence of ecven
    else:
        return [nums[0]] + remove_even(nums[1:]) # The recusrive call + the creation of new list

def even_list(nums):
    if nums == []:
        return []
    if nums[0]%2 != 0:
        return even_list(nums[1:])
    else:
        return [nums[0]] + even_list(nums[1:])
    
lst = [5,3,4,8,1,13,7,10]
res = remove_even(lst)
res_2 = even_list(lst)
print(res)
print(res_2)

