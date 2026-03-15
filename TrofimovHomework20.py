"""Напишите функцию, которая конвертирует температуру
из градусов Цельсия в Фаренгейты и наоборот.

Формулы для конвертации температур:
● Из градусов Цельсия в Фаренгейты:
F = C * 9/5 + 32
● Из градусов Фаренгейта в Цельсия:
C = (F-32) * 5/9

Данные:
temp = 100
scale = "C"
Конвертер температуры
Пример вывода:
100C = 212.0F"""

def degree_convertor(temp, scale="C"):
    if scale == "C":
        return print(f"{temp}{scale} = {temp * 9/5 + 32}F")
    return print(f"{temp}{scale} = {(temp - 32) * 5/9}C")

degree_convertor(100)
degree_convertor(100, "C")
degree_convertor(100, scale="C")
degree_convertor(212, "F")

"""Создайте функцию filter_strings, которая принимает
целое число n и любое количество строк (по
отдельности, а не как коллекция).
Функция должна возвращать список строк, длина
которых больше n.
Данные:
strings = ["apple", "banana", "cherry", "date",
"fig"]
n = 5
Пример вывода:
['banana', 'cherry']"""

def filter_strings(n, *args):
    # x = []
    # for word in args:
    #     if len(word) > n:
    #         x.append(word)
    # return x
    return [word for word in args if len(word) > n]

print(filter_strings(5,"apple", "banana", "cherry", "date", "fig"))

"""Напишите функцию, которая принимает число и
возвращает, является ли оно положительным,
отрицательным или нулём.
Данные:
num = -3
Пример вывода:
Число отрицательное"""

def prove_digit(num):
    # if num > 0:
    #     return "Число положительное"
    # if num < 0:
    #     return "Число отрицательное"
    # else:
    #     return "Число равно нулю"
    return ("Число положительное" if num > 0 else ("Число отрицательное" if num < 0 else "Число равно нулю"))

print(prove_digit(5))
print(prove_digit(-5))
print(prove_digit(0))

# Task I
"""Простое число
Напишите функцию, которая проверяет, является ли число n простым (делится только на 1 и само себя) и
возвращает булевый результат.
Данные:
n = 17
Пример вывода:
Число 17 является простым"""

# number = 17
# if number == 1:
#     res = False
# res = True
# for div in range(number - 1, 1, -1):
#     if not number % div:
#         res = False
#         break
# print(f"Число {number} является простым? {res}")

def is_number_simple(n):
    if n == 1:
        return False
    res = True
    for div in range(n - 1, 1, -1):
        if not n % div:
            res = False
            break
    return res

print(f"Число является простым? {is_number_simple(17)}")

# Task II

"""Фильтрация чисел по чётности
Напишите функцию, которая принимает filter_type ("even" или "odd") и произвольное количество чисел,
возвращая только те, которые соответствуют фильтру.
Пример вызова:
print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5, 7))
Пример вывода:
[2, 4, 6]
[15, 25]
Некорректный фильтр"""

def filter_numbers(key, *args):
    x = []
    if key == "even" or key == "odd":
        for digit in args:
            if key == "even" and not digit % 2:
                x.append(digit)
            elif key == "odd" and digit % 2:
                x.append(digit)
    else:
        return "Некорректный фильтр"
    return x

print(filter_numbers("even", 1, 2, 3, 4, 5, 6))
print(filter_numbers("odd", 10, 15, 20, 25))
print(filter_numbers("prime", 2, 3, 5))

# Task III

"""Напишите функцию, которая принимает любое количество словарей и объединяет их в один. Если ключи
повторяются, используется значение из последнего словаря.
Данные:
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}
Пример вызова:
print(merge_dicts(dict1, dict2, dict3))"""

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict3 = {"d": 5}

def merge_dicts(*args):
    res = {}
    for dictionary in args:
        for key, value in dictionary.items():
            res[key] = value
    return res

print(merge_dicts(dict1, dict2, dict3))

# x = dict1 | dict2 | dict3
# print(x)
#
# dicts = ({"a": 1, "b": 2}, {"b": 3, "c": 4}, {"d": 5})
#
# res = {}
# for dict in dicts:
#     for key, value in dict.items():
#         res[key] = value
# print(res)
