"1. Рамка-обводка"
import time

"""Создайте декоратор framed, который оборачивает результат в рамку из символов = длиной 40.

Пример применения:
@framed
def show_title():
    print("== Menu ==")

Пример вывода:
========================================
== Menu ==
========================================
"""

def framed(func):
    def wrapper():
        print("=" * 40)
        func()
        print("=" * 40)
    return wrapper

@framed
def show_title():
    print("== Menu ==")

show_title()

"2. Настраиваемая рамка-обводка"
"""Доработайте декоратор framed, чтобы он принимал параметр width, определяющий ширину рамки, и
параметр symbol, определяющий символ для рамки (по умолчанию "=").

Пример применения:
@framed(30, "-")
def show_title():
    print("== Menu ==")

Пример вывода:
------------------------------
== Menu ==
------------------------------"""

def framed(width: int, symbol: str="="):
    def decorator(func):
        def wrapper():
            print(symbol * width)
            func()
            print(symbol * width)
        return wrapper
    return decorator

@framed(30, "-")
def show_title():
    print("== Menu ==")

show_title()

"1. Среднее время выполнения"
"""Создайте декоратор measure_time, который измеряет и выводит среднее время
выполнения функции за 5 вызовов.
Функция может быть любой: например, сортировка списка, чтение из файла или
расчёты.

Пример применения:
@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total
    
Пример вывода:
Среднее время выполнения для 5 вызовов:
0.21 секунд
Результат: 49999995000000
"""
import time

def measure_time(func):
    total = []
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        this_run = time.time() - start
        total.append(this_run)
        if len(total) == 5:
            print(f"Среднее время выполнения для 5 вызовов:\n{sum(total)/5:.2f} секунд")
            total.clear()
            return f"Результат: {res}"
        return res
    return wrapper

@measure_time
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

print(compute())
print(compute())
print(compute())
print(compute())
print(compute())

"2. Среднее время выполнения с количеством вызовов"
"""Доработайте декоратор measure_time, чтобы он принимал параметр repeats —
количество вызовов функции.
Декоратор должен выполнять функцию указанное число раз и выводить среднее
время выполнения."""

import time

def measure_time(repeats: int):
    def decorator(func):
        def wrapper(*args, **kwargs):
            total = []
            for _ in range(repeats):
                start = time.time()
                res = func(*args, **kwargs)
                this_run = time.time() - start
                total.append(this_run)
            print(f"Среднее время выполнения для {repeats} вызовов:\n{sum(total)/repeats:.2f} секунд")
            total.clear()
            return f"Результат: {res}"
        return wrapper
    return decorator

@measure_time(10)
def compute():
    total = 0
    for i in range(10_000_000):
        total += i
    return total

print(compute())

