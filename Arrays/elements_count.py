count_dict = {}
nums = [3,5,3,6,1,8,1,2,3,5,6,8]
for i in nums:
    if i % 2 == 0:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1

print(count_dict)