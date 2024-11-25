def largest_secondlargest(nums):
    if len(nums) < 2:
        return "List contains less than 2 elements"
    
    lrg = scd_lrg = -1000

    for num in nums:

        if num > lrg:
            scd_lrg = lrg
            lrg = num
        elif num > scd_lrg and scd_lrg != lrg:
            scd_lrg = num
        
    if scd_lrg == -1000:
        return "All elements are same"
    
    return f"Largest : {lrg}, Second Largest : {scd_lrg}"

my_list = [4,6,3,7,8,3,6,8,12,3,4,9,2]
print(largest_secondlargest(my_list))
        