lst = [4, 5, 6, 7, 8, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 1, 2]

curr_sublist = []
res_list = []

for i in range(len(lst)):

    if not curr_sublist or lst[i] > curr_sublist[-1]:
        curr_sublist.append(lst[i])
    else:
        if len(curr_sublist) > 1:
            res_list.append(curr_sublist)
        curr_sublist = [lst[i]]
if len(curr_sublist) > 1:
    res_list.append(curr_sublist)

print(res_list)
print(max(res_list,key=len))