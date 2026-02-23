# # Task I
#
# """
# Напишите программу, которая создаёт новый кортеж, состоящий из элементов
# изначального в том же порядке.
# Добавить в него только элементы, которые больше всех предыдущих значений
# в исходном кортеже.
# """
#
numbers = (3, 7, 2, 8, 5, 10, 1)
"Var I"
res = []

for index, item in enumerate(numbers):
    if index < 1 or item > max(numbers[:index]): # Тут исправил с max(res), мне кажется так
        res.append(item)                         # больше соответствует условию задачи.
res = tuple(res)
print(f"Кортеж по возрастанию: {res}")

# "Var II"
# res = []
#
# for index in range(len(numbers)):
#     if index < 1 or numbers[index] > max(numbers[:index]):
#         res.append(numbers[index])
# res = tuple(res)
# print(f"Кортеж по возрастанию: {res}")

# Task II
"""
Напишите программу, которая находит индексы элементов кортежа,
встречающихся более одного раза.
Вывести сами элементы и их индексы.
"""

numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
buffer = []

"Var IV"
for item in numbers:
    if numbers.count(item) > 1 and item not in buffer:
        target = item
        index_buffer = []
        for index, char in enumerate(numbers):
            if char == target:
                index_buffer.append(str(index))
        print(f"Индексы элемента {item}: {" ".join(index_buffer)}")
        buffer.append(item)

"Var III"
for item in numbers:
    if numbers.count(item) > 1 and item not in buffer:
        start = -1
        index_buffer = []
        for _ in range(numbers.count(item)):
            index = numbers.index(item, start + 1)
            index_buffer.append(str(index))
            start = index
        print(f"Индексы элемента {item}: {" ".join(index_buffer)}")
        buffer.append(item)

# "Var II"
# for item in numbers:
#     if numbers.count(item) > 1 and item not in buffer:
#         count = len(numbers) - item
#         buffer.append(item)
#         print(f"Индексы элемента {item}:", end="\t")
#         for i in range(len(numbers)):
#             start = 0
#             index = 0
#             if numbers[i] == item:
#                 while True:
#                     if start + 1 >= len(numbers) - 1:
#                         break
#                     else:
#                         index = numbers.index(item, start + 1)
#                         print(index, end=" ")
#                         start = index
#         print()

"Var I"
# for index, item in enumerate(numbers):
#     count = len(numbers) - index
#     if numbers.count(item) > 1 and item not in buffer:
#             print(f"Индексы элемента {item}:", end="\t")
#             while count != 0:
#                 if item == numbers[index]:
#                     print(index, end=" ")
#                 index += 1
#                 count -= 1
#             print()
#     buffer.append(item)


