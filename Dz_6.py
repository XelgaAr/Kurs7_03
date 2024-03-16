# [12, 3, 4, 10] => [10, 12, 3, 4]
# [1] => [1]
# [] => []
# [12, 3, 4, 10, 8] => [8, 12, 3, 4, 10]'

first_list = [12, 3, 4, 10]
# first_list = [1]
# first_list = []
# first_list = [12, 3, 4, 10, 8]


if len(first_list)== 0 :
    print([])
else:
    a = first_list.pop()
    # print([a] + first_list)
    first_list.insert(0, a)
    print(first_list)