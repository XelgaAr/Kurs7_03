# [1, 2, 3, 4, 5, 6] => [[1, 2, 3], [4, 5, 6]]
# [1, 2, 3] => [[1, 2], [3]]
# [1, 2, 3, 4, 5] => [[1, 2, 3], [4, 5]]
# [1] => [[1], []]
# [] => [[], []]

lst=[1,2,3,4,5,6]
# lst=[1, 2, 3]
# lst=[1, 2, 3, 4, 5]
# lst=[1]
# lst=[]

l = int(len(lst) / 2)
if len(lst) % 2 == 0:
    lst1 = lst[:l]
    lst2 = lst[l:]
    lst1_lst2 = [lst1, lst2]
    print(lst1_lst2)
else:
    lst1 = lst[:l+1]
    lst2 = lst[l+1:]
    lst1_lst2 = [lst1, lst2]
    print(lst1_lst2)
