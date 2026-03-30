"Обработка ввода пользователя"
"""Напишите программу, которая запрашивает у
пользователя число и обрабатывает возможные
ошибки ввода, пока не получит корректное
число.
Пример вывода
Введите число: qwe
Ошибка: Введите корректное число.
Введите число: 12.5
Вы ввели число: 12.5"""

while True:
    try:
        number = float(input("Введите число: "))
    except ValueError as e:
        print(f"Введите корректное число. Ошибка: {e}")
    else:
        print(f"Вы ввели число: {number}")
        break

"Проверка возраста"
"""Напишите функцию, которая проверяет, что
возраст пользователя не меньше 18 лет с
использованием ошибок
Пример вывода
Введите возраст: 17
Ошибка: Возраст должен быть 18 лет и старше."""

# try:
#     your_age = int(input("Введите возраст: "))
#     if your_age < 18:
#         raise ValueError("Ошибка: Возраст должен быть 18 лет и старше.")
# except ValueError as e:
#     print(e)
# else:
#     print("Всё ок :)")

def age_checker(your_age: int) -> str:
    if your_age < 18:
        raise ValueError(f"Ошибка: Возраст должен быть 18 лет и старше. Текущий: {your_age}")
    return f"Всё ок :). Ваш возраст: {your_age}"

try:
    print(age_checker(17))
except ValueError as e:
    print(e)

# Task I
"Деление без ошибок"
"""Напишите функцию, которая выполняет деление двух чисел, введенных пользователем, и
обрабатывает возможные ошибки.

Пример вывода:
Введите делимое: 345
Введите делитель: 5a
Ошибка: Введено некорректное число"""

def two_numbers_divider():
    try:
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        res = a / b
    except (ValueError, ZeroDivisionError):
        print("Ошибка: Введено некорректное число")
    else:
        print(f"Результат деления: {res}")

two_numbers_divider()

# Task II
"Логирование ошибок"
"""Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log в соответствии с форматом
ниже.
Пример вывода:
2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число."""

import logging
logging.basicConfig(filename="task2_trofimov.log",
                    format="%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s",
                    encoding="utf-8"
                    )

def two_numbers_divider():
    try:
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        res = a / b
    except (ValueError, ZeroDivisionError):
        logging.error("Ошибка: Введено некорректное число")
        print("Ошибка: Введено некорректное число")
    else:
        print(f"Результат деления: {res}")

two_numbers_divider()