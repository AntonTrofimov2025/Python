"""1. Список всех стран
Используя базу данных world, выведи названия всех стран из таблицы country.
Каждое название должно отображаться с новой строки и иметь номер.
Пример вывода:
1. Aruba
2. Afghanistan
3. Angola
...
239. Zimbabwe"""
import pymysql
import os
from dotenv import load_dotenv

load_dotenv('.env')

with pymysql.connect(
    host = os.environ.get("DB_HOST", "localhost"),
    user = os.environ.get("DB_USER", "user"),
    password = os.environ.get("DB_PASSWORD", "password"),
    database = "world"
) as conn:
    with conn.cursor() as cursor:
        cursor.execute("SELECT ROW_NUMBER() over (ORDER BY Name), Name FROM country")
        for row in cursor:
            print(f"{row[0]}. {row[1]}")

print()
"""2. Города выбранной страны
Добавьте к предыдущей программе возможность выбора страны. Пользователь
должен ввести название страны. Далее выведите все города этой страны и их
численность населения.
Пример вывода:
Введите страну: Germany
Berlin — 3386667
Hamburg — 1704735
Munich [München] — 1194560
..."""

import pymysql
import os
from dotenv import load_dotenv

load_dotenv('.env')

with pymysql.connect(
    host = os.environ.get("DB_HOST", "localhost"),
    user = os.environ.get("DB_USER", "user"),
    password = os.environ.get("DB_PASSWORD", "password"),
    database = "world"
) as conn:
    with conn.cursor() as cursor:
        your_country = input("Select your country: ").lower().title()
        cursor.execute("""SELECT c.Name, c.Population
                              FROM country ct
                              JOIN city c ON ct.Code = c.CountryCode
                              WHERE ct.Name = %s
                              ORDER BY c.Population DESC""", (your_country, ))
        all_data = cursor.fetchall()
        if all_data:
            for row in all_data:
                city, pop = row
                print(f"{city} - {pop}")
        else:
            print("Country not found")
