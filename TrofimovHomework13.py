# Task I

"""
Напишите программу, которая создаёт новый кортеж, состоящий из элементов
изначального в том же порядке.
Добавить в него только элементы, которые больше всех предыдущих значений
в исходном кортеже.
"""

numbers = (3, 7, 2, 8, 5, 10, 1)
"Var I"
res = ()

for index, item in enumerate(numbers, 0): # Ноль не обязателен, но я решил дописать.
    if index < 1 or item > max(res):      # Уж очень долго мучился я с этой первой задачей :\
        res += tuple([item])
print(f"Кортеж по возрастанию: {res}")

# "Var II"
# res = ()
#
# for index in range(0, len(numbers)):
#     if index < 1 or numbers[index] > max(numbers[:index]):
#         res += tuple([numbers[index]])
# print(f"Кортеж по возрастанию: {res}")

# Task II
"""
Напишите программу, которая находит индексы элементов кортежа,
встречающихся более одного раза.
Вывести сами элементы и их индексы.
"""

numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
buffer = []

for index, item in enumerate(numbers):
    count = len(numbers) - index
    if numbers.count(item) > 1 and item not in buffer:
            print(f"Индексы элемента {item}:", end="\t")
            while count != 0:
                if item == numbers[index]:
                    print(index, end=" ")
                index += 1
                count -= 1
            print()
    buffer.append(item)