# print(round(2.5))
# print(round(2.51))
#
# print(round(-2.5))
# print(round(-2.51))

# Task 1
"""Напишите программу, которая принимает число с плавающей точкой и
 округляет его до целого числа в соответствии с правилами школьной математики,
 а не банковского округления."""
import math
num1 = float(input("Введите вещественное число: "))

"Var I"
if num1 > 0:
    res1 = round(num1 + 0.01)
else:
    res1 = round(num1 - 0.01)

res2 = round(num1)

# "Var II"
# if num1 > 0:
#     res1 = math.ceil(num1)
# else:
#     res1 = math.floor(num1)
#
# res2 = round(num1)

print(f"Округленное значение: {res1}", f"Bank Style: {res2}")

# Task 2
"""Напишите программу, которая запрашивает у пользователя длины двух катетов
прямоугольного треугольника и вычисляет длину гипотенузы."""



a = float(input("Введите длину первого катета: "))
b = float(input("Введите длину второго катета: "))

# "Var I"
# c = math.sqrt(a ** 2 + b ** 2)
"Var II"
c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"Длина гипотенузы: {c}")


