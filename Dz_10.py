# _ => True
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

import keyword
import string

my_string = input('Введите название переменной: ')
is_ok = "_" == my_string or (my_string.islower() and not my_string[0].isdigit() and " " not in my_string)
is_not_ok = (my_string in keyword.kwlist
           or any(el in string.punctuation and el != "_" for el in my_string))

print(is_ok and not is_not_ok)
