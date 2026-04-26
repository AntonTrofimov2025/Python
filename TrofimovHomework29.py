"Фильтр чисел"
"""Создайте генератор, который принимает список чисел и выдаёт только числа, кратные 5.

Данные:
numbers = [12, 15, 33, 40, 55, 62, 75, 83, 90]

Пример вывода:
15
40
55
75
90"""

def gen_equal_5(nums):
    for num in nums:
        if not num % 5:
            yield num

numbers = [12, 15, 33, 40, 55, 62, 75, 83, 90]

gen = gen_equal_5(numbers)

for digit in gen:
    print(digit)

"Квадраты чисел"
"""Создайте генератор, который принимает число n и генерирует квадраты чисел от 1 до n включительно

Данные:
n = 10

Пример вывода:
1
4
9
16
25
36
49
64
81
100"""

def nums_gen(n):
    for num in range(1, n + 1):
        yield num ** 2

gen = nums_gen(10)

for num in gen:
    print(num)

"1. Генератор Фибоначчи"
"""Создайте генератор, который генерирует
последовательность Фибоначчи бесконечно,
возвращая по одному числу за раз.
Последовательность Фибоначчи — это ряд чисел,
где каждое следующее число равно сумме двух
предыдущих.
Начинается с 0 и 1.

Пример вывода:
0
1
1
2
3
5
8
13
21
34"""
from typing import Iterator

def fibonacci(a: int, b: int) -> Iterator[int]:
    """
    This iterator generates Fibonacci sequence starting from two given numbers.

    :param a: The first starting number of the sequence.
    :param b: The second starting number of the sequence.
    :return: Returns a generator object.
    """
    if not (isinstance(a, int) and isinstance(b, int)):
        raise TypeError("Arguments must be numbers only!")
    if a < 0 or b < 0:
        raise ValueError("Number cannot be negative.")
    while True:
        yield a
        a, b = b, a + b

try:
    gen = fibonacci(0, 1)

    for _ in range(10):
        print(gen.__next__())
except (ValueError, TypeError) as e:
    print(e)

"2. Генератор уникальных элементов"
"""Создайте генератор, который принимает список элементов и выдаёт только уникальные значения, сохраняя
порядок их появления в исходном списке

Данные:
data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

Пример вывода:
3
1
2
4
5
6
7
8"""
from typing import Iterator

def unique_elements(nums: list[int]) -> Iterator[int]:
    """
    The list of elements-accepting generator that's used to separate
    only unique values preserving its original order.

    :param nums: Put here your list of elements.
    :return: Returns a generator object.
    """
    if not isinstance(nums, list):
        raise TypeError("Argument must be a list!")
    if not all(isinstance(num, int) for num in nums):
        raise TypeError("All list elements must be int!")
    check = set()
    for num in nums:
        if num not in check:
            yield num
            check.add(num)

data = [3, 1, 2, 3, 4, 1, 5, 2, 6, 7, 5, 8]

try:
    gen = unique_elements(data)

    for num in gen:
        print(num)
except TypeError as e:
    print(e)