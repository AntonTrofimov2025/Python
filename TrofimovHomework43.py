"""1. Поиск заказов с маленькой суммой
Прочитайте все документы из коллекции orders, у которых сумма (amount) меньше 10. Выведите
каждый найденный заказ построчно.
Пример вывода:
{'_id': ObjectId('...'), 'id': 3, 'customer': 'Olga', 'product': 'Kiwi', 'amount':
9.6, 'city': 'Berlin'}
{'_id': ObjectId('...'), 'id': 5, 'customer': 'Olga', 'product': 'Banana', 'amount':
8, 'city': 'Madrid'}"""
from pymongo import MongoClient

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit")

db = client["ich_edit"]

orders = db["orders"]

for order in orders.find({"amount": {"$lt": 10}}):
    print(order)

"""Сохранение результатов в другую коллекцию
Сохраните все найденные заказы в новую коллекцию orders_lesson_43. После записи выведите, сколько
документов было добавлено.
Пример вывода:
6 documents inserted into 'orders_lesson_43'."""

found_orders = orders.find({"amount": {"$lt": 10}})

new_collection = db["orders_lesson_43_anton_t"]

try:
    res = new_collection.insert_many(found_orders)
    count = len(res.inserted_ids)
    print(f"{count} documents inserted into 'orders_lesson_43_anton_t'.")
except Exception as e:
    print("InvalidOperation:", e)

# count = new_collection.count_documents({})

"""1. Добавление товаров
Создайте программу, которая подключается к MongoDB и:
● выбирает базу ich_edit и коллекцию
products_<your_group>_<your_full_name>
● очищает коллекцию перед началом
● добавляет 3 товара с полями: name, price, stock
● выводит сообщение о количестве добавленных товаров
Пример вывода:
3 products inserted."""

"""2. Увеличение цен
Продолжите предыдущую задачу. Теперь программа должна:
● увеличить цену всех товаров на 20%
● вывести количество обновлённых записей
● затем вывести список всех товаров с новыми ценами
Пример вывода:
Prices updated for 3 products.
Updated products:
- Pen — $1.80
- Notebook — $4.79
- Backpack — $30.00"""

from pymongo import MongoClient

client = MongoClient(
    "mongodb://ich_editor:verystrongpassword"
    "@mongo.itcareerhub.de/?readPreference=primary"
    "&ssl=false&authMechanism=DEFAULT&authSource=ich_edit")

db = client["ich_edit"]
products = db["products_121225ptm_anton_t"]

products.delete_many({})

new_items = [{"name": "Pen", "price": 1.50, "stock": 4},
             {"name": "Notebook", "price": 4, "stock": 4},
             {"name": "Backpack", "price": 25, "stock": 4}]

res = products.insert_many(new_items)
count = len(res.inserted_ids)

print(f"{count} products inserted.")

updated_items = products.update_many({}, [{"$set": {"price": {"$round": [{"$multiply": ["$price", 1.2]}, 2]}}}])
print(f"Prices updated for {updated_items.modified_count} products")

res = products.find()
print("Updated products:", *(f'- {doc["name"]} — ${doc["price"]:.2f}' for doc in res), sep="\n")
