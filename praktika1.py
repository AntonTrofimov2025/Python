# a = int(input('Enter a number: '))
# b = int(input('Enter a number: '))
#
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print('Division by null is impossible!!')

# x = y = z = 10
# x = 10
# y = 10
# z = 10
#
# x = 5
# y = 6
# res = 5/6
# print(type(res))
#
# num = 5
# num + 3
# print(num)
#
# "Здесь получится 5, т.к. новое значение не присвоено num"
#
# num = 5
# num = num + 3
# print(num)
#
# "Здесь получится 8, т.к. к num новое значение присвоено"
#
#
# num = 5
# num += 3
# print(num)
# "Тоже получится, т.к. += это тоже самое что num = num + 3, только из C++"
#
#
# print('a / b = ... , enter your a and b: ')
# a = int(input())
# b = int(input())
# num = a // b
# print(num)
# print("""
# If you print, for instance, -5 divided by 2, it'll result to -3,because
# the Python calculation system with "//", dividing numbers as integers,
# rounds numbers in direction of smaller ones and by that we also receive integer
# number
# """)

#
# print('a / b = ... , enter your a and b: ')
# a = float(input())
# b = float(input())
# num = a / b
# print(num)
# print("""
# Here we are usual numbers by standard mathematic
# and in case of -5 and 2 it results to -2.5
# # """)
#
# """Примеры множественного присваивания:
# 1) Общая логика в программировании
# 2) Логика Python
# """
#
# print('1 Example')
# a, b = 1, 2
# c = a
# a = b
# b = c
# print(a, b)
#
# print('2 Example')
# a, b = 1, 2
# a, b = b, a
# # print(a, b)
#
# res = 5
# print(res)
# print(type(res))
# res += 3.14
# print(res)
# print(type(res))

a = "10"
a = int(a)
print(a)
print(type(a))

a = int("10.0")
"Если строке выше вместо int написать float то заработает :)"
print(a)
print(type(a))