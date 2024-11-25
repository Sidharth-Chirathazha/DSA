def heapify(arr,n,parnt_idx):

    largest = parnt_idx
    left = (2*parnt_idx) + 1
    right = (2*parnt_idx) + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != parnt_idx:
        arr[largest],arr[parnt_idx] = arr[parnt_idx],arr[largest]
        heapify(arr,n,largest)

def heapsort(arr):

    n = len(arr)

    for i in range(n//2,-1,-1): #Buid Heap Function
        heapify(arr,n,i)

    for j in range(n-1,0,-1):
        arr[j],arr[0] = arr[0],arr[j]
        heapify(arr,j,0)


lst = [4,8,12,9,13,2,5]
heapsort(lst)
print(lst)