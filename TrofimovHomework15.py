# Task I

"""1. Одно слово
Напишите программу, которая обрабатывает список из строк и удаляет все строки,
содержащие более одного слова, а также преобразует оставшиеся строки к нижнему регистру."""

text_list = ["Hello", "Python Programming", "World", "Advanced Topics", "Simple"]

# "Var II"
# cache = []
#
# for item in text_list[:]:
#     if len(item.split()) > 1:
#         cache.append(item)
#     else:
#         index = text_list.index(item)
#         text_list[index] = item.lower()
# x = 0
# for item in range(len(cache)):
#     text_list.remove(cache[x])
#     x += 1

"Var I"
for item in reversed(text_list):
    if len(item.split()) > 1:
        text_list.remove(item)
    else:
        index = text_list.index(item)
        text_list[index] = item.lower()

print(f"Обработанный список: {text_list}")

# Task II

"""2. Обновление цен товаров
Дан список товаров с ценами. Программа должна применить скидку
к каждому товару и добавить в список элемент с новой ценой.
В конце вывести таблицу с новой ценой."""

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

percent = int(input("Введите скидку (в процентах): "))
discount = (100 - percent) / 100

print(f"{"Товар":<10} {"Старая цена":>15} {"Новая цена":>20}")

for item in products:
    product, price = item
    print(f"{product:<10} {price:>14.2f}$ {price*discount:>19.2f}$")





"BONUS, side task from lesson"
"""Фильтрация элементов в группах

Напишите программу, которая создаёт копию вложенного списка. Затем в копии
необходимо удалить элементы, которые меньше среднего значения всех элементов
вложенного списка. Убедитесь, что исходный список остался неизменным."""
import copy

nested_list = [[10, 15, 20], [5, 25, 30], [35, 40, 80]]
deep_copy = copy.deepcopy(nested_list)
elements = []

"More effective version"
for item in deep_copy:
    avg_value = sum(item) / len(item)
    for i in range(len(item) -1, -1, -1):
        if item[i] < avg_value:
            item.pop(i)

# "Old version"
# for item in deep_copy:
#     avg_value = sum(item) / len(item)
#     for element in reversed(item):
#         if element < avg_value:
#             item.remove(element)

# indexes = []
#
# for item in deep_copy:
#     ind = 0
#     avg_value = sum(item) / len(item)
#     for index, element in enumerate(item):
#         if element < avg_value:
#             indexes.append(index)
#             # item.remove(element)
#             # item.remove(item[index])
#     count = len(indexes)
#     while count != 0:
#         item.remove(item[indexes[ind]])
#         ind += 1
#         count -= 1
#     indexes.clear()

print(f"Исходный список: {nested_list}")
print(f"Глубокая копия после изменений: {deep_copy}")
