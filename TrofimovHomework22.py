"Список квадратов чисел"
"""Напишите функцию, которая сформирует список квадратов из
полученного списка, без использования циклов или списковых
включений.

Пример вывода:
[1, 4, 9, 16, 25]"""

numbers = [1, 2, 3, 4, 5]

print(list(map(lambda x: x ** 2, numbers)))

"Сортировка по возрасту"
"""Отсортируйте список кортежей (имя, возраст) по возрасту.

Пример вывода:
[('Mike', 19), ('Isabella', 19), ('Henry', 19), ('Bob', 20), ('Charlie', 23), ('Jack',
24), ('Alice', 25), ('Grace', 27), ('Kevin', 28), ('Eve', 29), ('Diana', 30), ('Laura',
31), ('Oscar', 33), ('Frank', 33), ('Nancy', 35)]"""

people = [
    ("Mike", 19), ("Nancy", 35), ("Charlie", 23), ("Oscar", 33), ("Eve", 29),
    ("Frank", 33), ("Bob", 20), ("Grace", 27), ("Isabella", 19), ("Jack", 24),
    ("Alice", 25), ("Kevin", 28), ("Laura", 31), ("Diana", 30), ("Henry", 19)
]

print(list(sorted(people, key=lambda x: x[1])))

"Сортировка по возрасту и имени"
"""Отсортируйте список кортежей (имя, возраст) по убыванию возраста, в рамках одинакового возраста
отсортируйте также по имени по алфавиту.

Пример вывода:
[('Nancy', 35), ('Frank', 33), ('Oscar', 33), ('Laura', 31), ('Diana', 30), ('Eve',
29), ('Kevin', 28), ('Grace', 27), ('Alice', 25), ('Jack', 24), ('Charlie', 23),
('Bob', 20), ('Henry', 19), ('Isabella', 19), ('Mike', 19)]"""

people = [
    ("Mike", 19), ("Nancy", 35), ("Charlie", 23), ("Oscar", 33), ("Eve", 29),
    ("Frank", 33), ("Bob", 20), ("Grace", 27), ("Isabella", 19), ("Jack", 24),
    ("Alice", 25), ("Kevin", 28), ("Laura", 31), ("Diana", 30), ("Henry", 19)
]

names = sorted(people, key=lambda x: x[0])
print(list(sorted(names, key=lambda x: x[1], reverse=True)))

# Task I
"Выбор заказов"
"""У вас есть список заказов. Каждый заказ содержит название продукта и его цену. Напишите функцию, которая:
1. Отбирает заказы дороже 500.
2. Создаёт список названий отобранных продуктов в алфавитном порядке.
3. Возвращает итоговый список названий.
Пример вывода:
['Chair', 'Laptop']"""

orders = [
    {"product": "Laptop", "price": 1200},
    {"product": "Mouse", "price": 50},
    {"product": "Keyboard", "price": 100},
    {"product": "Monitor", "price": 300},
    {"product": "Chair", "price": 800},
    {"product": "Desk", "price": 400}
]

x = sorted(map(lambda x: x["product"], filter(lambda x: x["price"] > 500, orders)))
print(x)

def sorting_orders(worterbuch_bitte):
    # res = []
    # for item in worterbuch_bitte:
    #     if item["price"] > 500:
    #         res.append(item["product"])
    # return sorted(res)
    # return sorted([item["product"] for item in worterbuch_bitte if item["price"] > 500]) # This is the best, but modified into lambda-var. Line75
    return sorted(map(lambda x: x["product"], filter(lambda x: x["price"] > 500, worterbuch_bitte)))

print(sorting_orders(orders))

# OLD, NOT ACTUAL
# ":)"
# x = map(lambda x: x["product"] if x["price"] > 500 else "", orders)
# x = filter(None, x)
# x = sorted(x)
# print(x)

# Task II
"Статистика продаж"
"""Дан список продаж в виде кортежей (товар, количество, цена).
Напишите программу, которая:
1. Вычисляет общую выручку для каждого товара.
2. Возвращает словарь с товарами {товар: выручка}, отсортированный по убыванию выручки.

Пример вывода:
{'Chair': 16000, 'Laptop': 6000,
'Monitor': 3000, 'Keyboard': 1500,
'Mouse': 1000}"""

sales = [
 ("Laptop", 5, 1200),
 ("Mouse", 50, 20),
 ("Keyboard", 30, 50),
 ("Monitor", 10, 300),
 ("Chair", 20, 800)
]

def revenue_calc(arg):
    # res = {}
    # for item in arg:
    #     res[item[0]] = item[1] * item[2]
    # return dict(sorted(res.items(), key=lambda x: x[1], reverse=True))
    return dict(sorted([(item[0], item[1] * item[2]) for item in arg], key=lambda x: x[1], reverse=True))
print(revenue_calc(sales))

":)"
print(dict(sorted(map(lambda x: (x[0], x[1] * x[2]), sales), key=lambda x: x[1], reverse=True)))