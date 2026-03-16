"""Частотный анализ слов
Напишите программу, которая подсчитывает количество вхождений каждого слова в тексте.
Программа должна игнорировать регистр слов и символы . и ,.

Пример вывода:
{'this': 2, 'is': 2, 'a': 2, 'test': 3, 'only': 1}"""

from collections import Counter
text = "This is a test. This test is only a test."
text = text.replace(".", "").replace(",", "")
text = text.lower().split()
text = Counter(text)
print(text)

"""Список студентов по факультетам
Напишите программу, которая принимает список студентов и их факультетов (кортежи) и
группирует студентов по факультетам в словарь.

Пример вывода:
Факультеты и студенты:
Физика: ['Иван', 'Пётр', 'Наталья']
Математика: ['Мария', 'Анна']
Информатика: ['Олег']"""

from collections import defaultdict

students = [
 ("Иван", "Физика"),
 ("Мария", "Математика"),
 ("Пётр", "Физика"),
 ("Анна", "Математика"),
 ("Олег", "Информатика"),
 ("Наталья", "Физика"),
]
print("Факультеты и студенты:")
res = defaultdict(list)

for name, subject in students:
    res[subject].append(name)

for subject, names in res.items():
    print(f"{subject}: {names}")

# Task I
"""Повторения букв
Реализуйте функцию, которая принимает текст и возвращает словарь с подсчётом количества каждой буквы,
игнорируя регистр.

Пример вывода:
{'p': 1, 'r': 2, 'o': 1, 'g': 2, 'a': 1, 'm': 2, 'i': 2, 'n': 2, 's': 1, 'f': 1, 'u': 1}"""

"Var III: Final"
from collections import Counter
text = "Programming is fun!"

def counter_analog(element):
    letters = [char.lower() for char in element if char.isalpha()]
    return dict(Counter(letters))

print(counter_analog(text))

"Var II: too saucy :D"
# text = "Programming is fun!"
#
# def counter_analog(element):
#     element = element.replace("!", "").replace(" ", "").lower()
#     from collections import Counter
#     element = Counter(element)
#     return element
#
# print(dict(counter_analog(text)))

"Var I"
# from collections import Counter
# text = "Programming is fun!"
# text = text.replace("!", "").replace(" ", "").lower()
# text = dict(Counter(text))
# print(text)

# Task II
"""Группировка студентов по классам
Создайте структуру для группировки студентов по классам.
Добавьте студентов в соответствующие группы.

Пример вывода:
{'class1': ['Alice', 'Charlie'], 'class2': ['Bob'], 'class3': ['Daisy']}"""
from collections import defaultdict

students = [("class1", "Alice"), ("class2", "Bob"), ("class1", "Charlie"), ("class3",
"Daisy")]
res = defaultdict(list)

for klass, name in students:
    res[klass].append(name)

print(dict(res))

