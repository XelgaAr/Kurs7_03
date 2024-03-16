what = input( "Что делаем? (+, -, *, /) : ")
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
if what == "+":
    c = a + b
    print("Результат: " + str(c))
elif what == "-":
    c = a - b
    print("Результат: " + str(c))
elif what == "*":
    c = a * b
    print("Результат: " + str(c))
elif what == "/"  and b == 0:
    print("Нельзя делить на 0 !")
elif what == "/":
    c = a / b
    print("Результат: " + str(c))