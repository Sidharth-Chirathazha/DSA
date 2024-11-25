def remove_even(data_list):
    if len(data_list) == 0:
        return "The list is empty"
    else:
       data_list = [x for x in data_list if x%2 != 0]
       
    return data_list

if __name__ == '__main__':

    nums_list = [2,4,7,8,1,4,9]
    res = remove_even(nums_list)
    print(res)