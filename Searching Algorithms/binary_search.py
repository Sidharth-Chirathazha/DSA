def binary_search(data_list,value):

    min = 0
    max = len(data_list) - 1

    while min<=max:
        mid = (min + max)//2

        if data_list[mid] == value:
            return f"item '{value}' found at index {mid}"
        elif data_list[mid] < value:
            min = mid + 1
        else:
            max = mid - 1
    return f"Item not found"
    
if __name__ == '__main__':

    result = binary_search([2,3,6,8,10,15],10)
    print(result)