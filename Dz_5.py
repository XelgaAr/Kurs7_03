# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

# lst=[1,2,3,4,5,6]
# lst=[1, 2, 3]
# lst=[1, 2, 3, 4, 5]
# lst=[1]
lst=[]

if len(lst) % 2 == 0:
    l = int(len(lst) / 2)
    lst1 = lst[:l]
    lst2 = lst[l:]
    lst1_lst2 = [lst1, lst2]
    print(lst1_lst2)
elif len(lst) % 2 != 0:
    l = int(len(lst) / 2) + 1
    lst1 = lst[:l]
    lst2 = lst[l:]
    lst1_lst2 = [lst1, lst2]
    print(lst1_lst2)
