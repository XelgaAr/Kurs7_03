# [0, 1, 7, 2, 4, 8] => (0 + 7 + 4) * 8 = 88
# [1, 3, 5] => 30
# [6] => 36
# # [] => 0
# [0, 1, 7, 2, 4, 8]
# [1, 3, 5]
# [6]
# []
first_list =[0, 1, 7, 2, 4, 8]

if len(first_list)== 0 :
    print([])
else:
    list1 = first_list[::2]
    list2 = first_list[-1]
    print((sum(list1))*list2)

