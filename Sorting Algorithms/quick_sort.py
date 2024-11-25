def quick_sort(arr):

    length = len(arr)

    if length <= 1:
        return arr
    else:
        middle = len(arr)//2
        pivot = arr.pop(middle)

    greater_items = []
    lesser_items = []

    for i in arr:
        if i > pivot:
            greater_items.append(i)
        else:
            lesser_items.append(i)
    
    return quick_sort(lesser_items) + [pivot] + quick_sort(greater_items)

lst = [4,2,8,1,9,14,3,16]
print(quick_sort(lst))