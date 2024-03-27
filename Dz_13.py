# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA
import string

result = ""
my_string = input('enter letters:')
ins = my_string.split("-")
a = ins[0]
b = ins[1]
c = string.ascii_letters.index(a)
d = string.ascii_letters.index(b)
e = range(c, d + 1)
for el in e:
    result += string.ascii_letters[el]
print(result)
