
# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59
# Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек. Тобто використовуючи функцію divmod або методи поділу // і % вам необхідно знайти відповідну кількість днів, годин, хвилин, а те що залишиться - це секунди, які менше 60 ;)

total_sec = int(input('введите число:'))
days, rest_sec = divmod(total_sec, 24 * 60 * 60)
hours, rest_sec = divmod(rest_sec, 60 * 60)
minutes, rest_sec = divmod(rest_sec, 60)

d = "днів"
d1 = "день"
d2 = "дні"
d_max = list(range(100))
last_number = int(str(days)[-1])
d_result = d

if days in d_max[11:15]:
    d_result = d
elif days in d_max[2:5] or last_number in d_max[2:5]:
    d_result = d2
elif days == 1 or last_number == 1:
    d_result = d1
print(f" {days} {d_result} {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(rest_sec).zfill(2)}")