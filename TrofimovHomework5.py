# Task 1

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

if num3 < num1 > num2:
    res3 = num1
elif num1 < num2 > num3:
    res3 = num2
elif num2 < num3 > num1:
    res3 = num3

if num3 > num1 < num2:
    res1 = num1
elif num1 > num2 < num3:
    res1 = num2
elif num2 > num3 < num1:
    res1 = num3

if num1 < num2 and num1 > num3 or num1 > num2 and num1 < num3:
    res2 = num1
elif num2 < num1 and num2 > num3 or num2 > num1 and num2 < num3:
    res2 = num2
elif num3 < num1 and num3 > num2 or num3 > num1 and num3 < num2:
    res2 = num3

print("Числа в порядке возрастания: ", res1, ",", res2, ",", res3)

# # Task 2
# print("Нужно узнать, является ли год високосным.")
#
# year = int(input("Введите год: "))
# "Var I"
# # if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
# #     print("Год является високосным.")
# # else:
# #     print("Год невисокосный.")
# "Var II"
# # print("Год является високосным." if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "Год невисокосный.")
#
# "Var III"
# match year:
#     case _ if year % 4 == 0 and year % 100 != 0:
#         print("Год является високосным.")
#     case _ if year % 400 == 0:
#         print("Год является високосным.")
#     case _:
#         print("Год невисокосный.")
