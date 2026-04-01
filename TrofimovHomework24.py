"Функция deepcopy"
"""Реализуйте аналог deepcopy() с помощью рекурсии.
Не забудьте проверить, чтобы изменения в копии не затронули оригинал.
Пример вывода:
Исходный: [[1, 2, 3], (4, [5, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]
Копия: [[1, 2, 3], (4, [0, 6], {8, 7}), {'a': 9, 'b': [10, 11]}, 'Hello', [12, (13, 14)], 15.5, 5]"""

original_data = [
        [1, 2, 3], # Вложенный список
        (4, [5, 6], {7, 8}), # Кортеж с вложенными структурами
        {"a": 9, "b": [10, 11]}, # Словарь со списком
        "Hello", # Строка
        [12, (13, 14)], # Список с кортежем
        15.5, # Число с плавающей точкой
        5 # Целое число
        ]


from typing import Any
def copyruem(obj):
    if isinstance(obj, list):
        return [copyruem(item) for item in obj]
    if isinstance(obj, dict):
        return {key: copyruem(value) for key, value in obj.items()}
    if isinstance(obj, tuple):
        return tuple(copyruem(item) for item in obj)
    if isinstance(obj, set):
        return set(copyruem(item) for item in obj)
    return obj

res = copyruem(original_data)
res[1][1][0] = 0
print(f"Исходный: {original_data}")
print(f"Копия: {res}")

# Task I
"Сумма цифр числа"
"""Напишите рекурсивную функцию, которая находит сумму всех цифр числа.
Данные:
num = 43197
Пример вывода:
24"""

"Var I"
num = 43197
def sum_of_all_numbers(your_number: int) -> int:
    if your_number < 10:
        return your_number
    last_number = your_number % 10
    remained_part = your_number // 10
    return last_number + sum_of_all_numbers(remained_part)

print(sum_of_all_numbers(num))

"Var 0"
# num = 43197
# from functools import reduce
# def sum_of_all_numbers(your_number: int) -> int:
#     your_number = [int(digit) for digit in str(your_number)]
#     return reduce(lambda x, y: x + y, your_number)
#
# print(sum_of_all_numbers(num))

# Task II
"Сумма вложенных чисел"
"""Напишите рекурсивную функцию, которая суммирует все числа во вложенных списках.
Данные:
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
Пример вывода:
28"""

"Var 0"
from typing import Any
nested_numbers = [1, [2, 3], [4, [5, 6]], 7]

def sum_of_int_lists(obj: list[Any]) -> int:
    if not obj:
        return 0
    if isinstance(obj[0], list):
        sum = sum_of_int_lists(obj[0])
    else:
        sum = obj[0]
    return sum + sum_of_int_lists(obj[1:])

print(sum_of_int_lists(nested_numbers))

"Var I"
# from typing import Any
# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
#
# def sum_of_int_lists(lst: list[Any]) -> int:
#     res = 0
#     for item in lst:
#         if isinstance(item, int):
#             res += item
#         else:
#             res += sum_of_int_lists(item)
#     return res
#
# print(sum_of_int_lists(nested_numbers))

"Var II"
# from typing import Any
# nested_numbers = [1, [2, 3], [4, [5, 6]], 7]
#
# def sum_of_int_lists(lst: list[Any]):
#     res = []
#     for item in lst:
#         if isinstance(item, list):
#             res.extend(sum_of_all_numbers(item))
#         else:
#             res.append(item)
#     return res
#
# print(sum_of_int_lists(nested_numbers))


