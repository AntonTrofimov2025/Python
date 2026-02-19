# Task I

"""1. Число в конце
Напишите программу, которая создает новый список.
В него необходимо добавить только те строки из
исходного списка, в которых цифры находятся только в конце."""

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]
new_list = []
index = []
index2 = []

for item in strings:
    for i in item:
        if i.isdigit():
            index.append(item.index(i))
    for i2 in item[::-1]:
        if i2.isdigit():
            index2.append(item.index(i2))
        else:
            break
    if index2[::-1] == index:
        new_list.append(item)
    index.clear()
    index2.clear()

print(f"Строки с цифрами только в конце: {new_list}")

# Task II

"""2. Удаление кратных
Напишите программу, которая удаляет из списка все значения,
кратные числу, которое вводится
пользователем."""

numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]
print(f"Имеющиеся элементы: {numbers}")
x = int(input("Введите число для удаления кратных ему элементов: "))
new_list = []

for item in numbers:
    if item % x:
        new_list.append(item)

print(f"Список без кратных значений: {new_list}")

# Task III

"""3. Порядок четных
Напишите программу, которая формирует новый список чисел.
Добавьте в него все элементы исходного
списка, где:
● нечетные числа занимают те же позиции,
● чётные числа отсортированы между собой обратном порядке."""

numbers = [5, 2, 3, 8, 4, 1, 2, 7]
even = []
odd = []
index = []
start = 0
x = 0

for item in numbers:
    if item % 2:
        odd.append(item)
    else:
        even.append(item)
        index.append(numbers.index(item, start))
    start += 1

even.sort(reverse=True)

for item in even:
    odd.insert(index[x], item)
    x += 1

print(f"Список после сортировки: {odd}")