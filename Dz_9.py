# [1, 2, 3, 4, 5, 6, 7, 9] == [1, 3, 7]
# [1, 1, 2, 1] == [1, 2, 2]
# [6, 3, 7] == [6, 7, 3]

first_list = [6, 3, 7]
a = first_list[0:3:2]
a.append(first_list[-2])
print(a)