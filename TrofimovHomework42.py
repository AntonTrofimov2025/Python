"""Добавление товаров в таблицу
Напишите программу, которая подключается к базе данных market, затем:
● создаёт таблицу products, если она ещё не существует
● добавляет в неё несколько товаров (название и цена)
● выводит список товаров с их ценами
Данные:
products = [
 ("Notebook", 10.00),
 ("Pencil", 1.00),
 ("Bag", 25.00)
]
Пример вывода:
Products added:
1. Notebook — $10.00
2. Pencil — $1.00
3. Bag — $25.00"""

"""Массовое повышение цен
Продолжите предыдущую программу. Теперь:
● увеличьте цену всех товаров на 20%;
● выполните обновление с помощью одного UPDATE;
● выведите список товаров после изменения цен.
Пример вывода:
Prices updated.
Products after update:
1. Notebook — $12.00
2. Pencil — $1.20
3. Bag — $30.00"""

products = [
    ("Notebook", 10.00),
    ("Pencil", 1.00),
    ("Bag", 25.00)
]

import os

import pymysql
from dotenv import load_dotenv

load_dotenv(".env_edit")

def is_increase():
    while True:
        mod = input("You wanna increase or decrease? (d/i): ").lower().strip()
        if mod in ("i", "d"):
            return mod == "i"
        print("Please choose between 'i' and 'd'")

def behaviour(is_increase):
    while True:
        try:
            percent = int(input("By what percent? "))
            if 1 <= percent <= 100:
                return percent / 100 + 1 if is_increase else 1 - percent / 100
            print("Percentage must be int only and between 1 and 100!!")
        except ValueError:
            print("Please enter a valid integer number!")

with pymysql.connect(host = os.environ.get("DB_HOST", "localhost"),
                     user = os.environ.get("DB_USER", "user"),
                     password = os.environ.get("DB_PASSWORD", "password"),
                     database = "market") as conn:
    with conn.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS products_anton_t (
                          id int auto_increment primary key,
                          product_name varchar(50),
                          price DECIMAL(10, 2)
                          )""")
        cursor.execute("DELETE FROM products_anton_t")
        cursor.execute("ALTER TABLE products_anton_t AUTO_INCREMENT = 1")
        print("All values in table products_anton_t have been hard reset!!")
        cursor.executemany("""INSERT INTO products_anton_t (product_name, price) VALUES (%s, %s)""", products)

        try:
            mass_price_update = input("Do you wanna update all prices? (y/n): ")
            if mass_price_update.lower().strip() == "y":
                your_choice = is_increase()
                what_percent = behaviour(your_choice)
                cursor.execute("UPDATE products_anton_t SET price = price * %s", (what_percent,))
                conn.commit()
                print('Prices updated.')
        except Exception as e:
            conn.rollback()
            print(f"Something went wrong: {e}")

        cursor.execute("SELECT * FROM products_anton_t")
        all_data = cursor.fetchall()

        print("Products added: ")
        for _id, prod_name, price in all_data:
            print(f"{_id}. {prod_name} - ${price}")
        conn.commit()

"""1. Создание базы
Напишите программу, которая:
● создаёт базу данных notes_app_<your_group>_<your_full_name>
● выбирает эту базу через USE notes_app
● выводит сообщение о результате
Пример вывода:
Database 'notes_app' created or already exists."""

"""2. Добавление заметок
Продолжите предыдущую программу:
● создайте таблицу notes с полями: id, title, content
● вставьте одну заметку в таблицу
● выполните commit() после вставки
● выведите все заметки используя DictCursor
Пример вывода:
Note added: Shopping list"""

import os

import pymysql
from pymysql.cursors import DictCursor
from dotenv import load_dotenv

load_dotenv(".env_edit")

with pymysql.connect(host=os.environ.get("DB_HOST", "localhost"),
                     user=os.environ.get("DB_USER", "user"),
                     password=os.environ.get("DB_PASSWORD", "password"),
                     cursorclass=DictCursor
                     ) as conn:
    with conn.cursor() as cursor:
        cursor.execute("CREATE DATABASE IF NOT EXISTS notes_app_121225ptm_anton_trofimov")
        cursor.execute("USE notes_app_121225ptm_anton_trofimov")
        print("Database 'notes_app_121225ptm_anton_trofimov' created or already exists.")
        cursor.execute("""CREATE TABLE IF NOT EXISTS notes
                          (
                              id      int auto_increment primary key,
                              title   varchar(25),
                              content varchar(100)
                          )""")
        cursor.execute("DELETE FROM notes")
        cursor.execute("ALTER TABLE notes AUTO_INCREMENT = 1")
        cursor.executemany("""INSERT INTO notes (title, content)
                              VALUES (%s, %s)""",
                           [
                               ("Shopping list", "Vodka, Seledka"),
                               ("Movies to watch", "The Day After Tomorrow"),
                               ("To do", "Don't forget to assemble a wardrobe you bought one month ago.")
                           ])
        conn.commit()
        cursor.execute("SELECT * FROM notes")
        all_data = cursor.fetchall()
        if all_data:
            for note in all_data:
                print(f"Note added: {note['title']}")
        else:
            print(" - Notes not found")