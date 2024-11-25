def count_of_elements(lst):

    count_dict = {}

    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    return count_dict


lst = [2,6,9,2,4,8,6,9,9,9,9,3,2,6,6,6]

result = count_of_elements(lst)
print(result)

first_highest = second_highest = -10
first_highest_item = second_highest_item = None

for key,value in result.items():
    if value > first_highest:
        second_highest,second_highest_item = first_highest,first_highest_item
        first_highest,first_highest_item = value,key
    elif value>second_highest:
        second_highest,second_highest_item = value,key

print({first_highest_item:first_highest,second_highest_item:second_highest})