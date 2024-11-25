def selection_sort(arr):

    for i in range(0,len(arr)-1):
        cur_min_indx = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[cur_min_indx]:
                cur_min_indx = j
        arr[i],arr[cur_min_indx] = arr[cur_min_indx],arr[i]

    return arr

lst = [4,7,2,9,1,3]
print(selection_sort(lst))