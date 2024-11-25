def linear_search(data_list,value):

    for i in range(0,len(data_list)):
        if data_list[i] == value:
            return f"Item '{value}' found at index {i}"
        
    return "Item not found"
    
if __name__ == '__main__':

    result = linear_search([1,3,5,6,8,9],6)
    print(result)