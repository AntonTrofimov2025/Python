"""Напишите программу, которая создает список из всех уникальных
символов строки, за исключением пробелов."""

text = "hello world"

# text = text.replace(" ", "")
text = "".join(text.split())

print(f"Уникальные символы: {set(text)}")

"""Напишите программу, которая принимает два списка
чисел и выводит список, содержащий элементы без
повторений, которые присутствуют в обоих списках."""

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

print(f"Элементы в обоих списках: {set(list1) & set(list2)}") # set(list1).intersection(set(list2))

# Task I
"Проверка на подмножество"
"""Напишите программу, которая проверяет, содержит ли первое множество
все элементы второго множества.
Реализуйте решение несколькими способами.
Решите одним из способов не используя возможности множеств."""

set1 = {1, 2, 3, 4}
set2 = {2, 3}

print("Пример вывода:", set1 >= set2)

# "With set options"
# if set1 >= set2:
#     success = True
# else:
#     success = False
#
# print("Пример вывода:")
# print(success)

"Without set options"
success = True
for i in set2:
    if i not in set1:
        success = False
        break

# success = None
# for i in set2:
#     if i in set1:
#         success = True
#     else:
#         success = False
#         break

print("Пример вывода:")
print(success)

# Task II

"Зеркальное подмножество"
"""Напишите программу, которая проверяет, являются ли элементы одного из множеств подмножеством
другого. В случае положительного ответа возвращает разницу между двумя множествами. Проверить
необходимо в обе стороны.
"""
set1 = {2, 3, 4, 5, 6}
set2 = {4, 5}
s2s1 = set2 <= set1
s1s2 = set1 <= set2

"Var II"
print(f"Является ли set2 подмножеством set1?: {s2s1}")
if s2s1:
    print(f"Разница: {set1 - set2}")
print(f"Является ли set1 подмножеством set2?: {s1s2}")
if s1s2:
    print(f"Разница: {set2 - set1}")

"Var I"
print(f"Является ли set2 подмножеством set1?: {s2s1}\n{"Разница: " if s2s1 else ""}"
      f"{set1 - set2 if s2s1 else ""}")

print(f"Является ли set1 подмножеством set2?: {s1s2}\n{"Разница: " if s1s2 else ""}"
      f"{set2 - set1 if s1s2 else ""}")