"Обработка элементов списка функцией"
"""Напишите функцию, которая принимает другую функцию и
список произвольных элементов. Примените переданную
функцию ко всем элементам списка и верните новый
список. Добавьте документацию и аннотации типов для всех
параметров и возвращаемого значения.
Данные:
numbers = [1, 2, 3, 4, 5]
Пример вывода:
[2, 4, 6, 8, 10]"""

numbers = [1, 2, 3, 4, 5]

def multiply_on_2(digit: int) -> int:
    """
    Multiplies one digit by two.

    :param digit: Please add an integer.
    :return: Returns multiplied result
    """
    return digit * 2

from typing import Callable
def func_launcher(func: Callable[[int], int], lst: list[int]) -> list[int]:
    """
    Applies func to each element of the list and returns new list.

    :param func: Which function would be applied.
    :param lst: Add your list.
    :return: Returns new list after function applying.
    """
    return [func(element) for element in lst]

print(func_launcher(multiply_on_2, numbers))

# Task I
"Объединение данных в строку"
"""Напишите функцию, которая принимает список любых данных (строки, числа, списки, словари) и возвращает
их строковое представление, объединённое через " | ". Добавьте документацию и аннотации типов для всех
параметров и возвращаемого значения.
Данные:
data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]
Пример вывода:
42 | hello | [1, 2, 3] | {'a': 1, 'b': 2}"""

data = [42, "hello", [1, 2, 3], {"a": 1, "b": 2}]

from typing import Any
def string_returner(lst: list[Any]) -> str:
    """
    This function transfers all elements of the list into one string, divided by Pipe (|).

    :param lst: List of any types of elements.
    :return: Returns string of list contents divided by Pipe.
    """
    return " | ".join([str(element) for element in lst])

print(string_returner(data))

# Task II
"Сумма вложенных чисел"
"""Напишите функцию, которая принимает список словарей, где каждый словарь содержит имя пользователя и
список баллов. Функция должна вернуть сумму всех чисел. Добавьте документацию и аннотации типов для
всех параметров и возвращаемого значения.
Данные:
data = [
 {"name": "Alice", "scores": [10, 20, 30]},
 {"name": "Bob", "scores": [5, 15, 25]},
 {"name": "Charlie", "scores": [7, 17, 27]}
]
Пример вывода:
Итоговый балл: 156"""

data = [
 {"name": "Alice", "scores": [10, 20, 30]},
 {"name": "Bob", "scores": [5, 15, 25]},
 {"name": "Charlie", "scores": [7, 17, 27]}
]

def score_calculator(lst: list[dict]) -> int:
    """
    This score calculator receives list of students with their own score and brings them into one total score.

    :param lst: List of students with scores presented in the form of a dictionary.
    :return: Returns total score put together from all scores of all students.
    """
    return sum([sum(element["scores"]) for element in lst])

print(score_calculator(data))