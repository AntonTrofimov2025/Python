"""Напишите программу, которая меняет местами ключи и значения в словаре.
Если значения повторяются, добавьте их в список.

Пример вывода:
Перевернутый словарь: {1: ['a', 'c'], 2: ['b'], 3: ['d']}"""

data = {"a": 1, "b": 2, "c": 1, "d": 3}

"Final"
out = {}

for key, value in data.items():
    out.setdefault(value, []).append(key)

print(out)

"Var II"
# res = {value: [key] for key, value in data.items()} # Не подойдет :\
#
# print(res)

"First var"
# out = {}
#
# for key, value in data.items():
#     if value not in out:
#         out[value] = [key]
#     else:
#         out[value].append(key)
#
# print(out)

"""Счётчик букв в словах
Напишите программу, которая подсчитывает количество каждой буквы в заданных словах и создаёт словарь,
где ключи — это слова, а значения — это ещё один словарь с подсчётом каждой буквы.

Пример вывода:
{'anna': {'a': 2, 'n': 2}, 'bennet': {'b': 1, 'e': 2, 'n': 2, 't': 1}, 'john': {'j': 1,
'o': 1, 'h': 1, 'n': 1}}"""

words = ["anna", "bennet", "john"]

"Second var"
res = {}
for word in words:
    value = {}
    for letter in word:
        "Advanced version"
        value[letter] = value.get(letter, 0) + 1
        "Just as example of more simple variation"
    #     if letter in value:
    #         value[letter] += 1
    #     else:
    #         value[letter] = 1
    res[word] = value

print(res)

"First var"
# res = {}
# for word in words:
#     value = {}
#     for letter in set(word):
#         how_many = word.count(letter)
#         value.setdefault(letter, how_many)
#     res.setdefault(word, value)
#
# print(res)

"Just text :)"
print({word: {letter: word.count(letter) for letter in set(word)} for word in words})

"""Распределение студентов по группам
У вас есть словарь, где ключи — имена студентов,
а значения — их баллы за экзамен.
Необходимо распределить студентов по группам:
● "Отличники": баллы >= 85
● "Хорошисты": баллы от 70 до 84
● "Троечники": баллы от 50 до 69
● "Не сдали": баллы < 50
Создайте словарь с ключами-группами и
словарями со студентами в качестве значений.

Пример вывода:
Распределение по группам:
{'Отличники': {'Аня': 92, 'Дима': 88},
'Хорошисты': {'Боря': 76}, 'Троечники':
{'Ваня': 65, 'Ева': 54}, 'Не сдали':
{'Галя': 48}}"""

students = {"Аня": 92, "Боря": 76,
"Ваня": 65, "Галя": 48, "Дима": 88,
"Ева": 54}

groups = [("Отличники", 85), ("Хорошисты", 70),
("Троечники", 50), ("Не сдали", 0)]

res = {}

for student, grade in students.items():
    for group in groups:
        group_name, threshold = group
        if grade >= threshold:
            res.setdefault(group_name, {})[student] = grade
            break

print(res)