def remove_dup(lst):

    unique_items = {}
    result = []

    for item in lst:

        if item not in unique_items:
            unique_items[item] = True
            result.append(item)

    return result

lst = [2,4,6,2,4,6,7,1,5,1,6]

print(remove_dup(lst))