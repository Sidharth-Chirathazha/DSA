def binary_search(lst,val,high,low):

    if high>=low:

        mid = (high+low)//2

        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            return binary_search(lst,val,high,mid+1)
        else:
            return binary_search(lst,val,mid-1,low)
    else:
        return -1

lst = [2,3,6,7,9,10]
val = 9
low = 0
high = len(lst)-1

res = binary_search(lst,val,high,low)

if res == -1:
    print(f"{val} not found in the list")
else:
    print(f"{val} found at index {res}")