"1. Расстояние между городами"
"""Создайте класс City, представляющий город с координатами.
● У каждого города есть поля name, latitude, longitude.
● Добавьте строковое представление объекта.
● Добавьте метод distance(city1, city2), который возвращает кортеж (latitude, longitude) между
двумя городами.
● Проверьте расстояние между двумя городами.
Пример вывода:
City: Berlin (52.52, 13.4)
City: Paris (48.85, 2.35)
Distance: 14.72
"""
import re

class City:
    def __init__(self, name, latitude, longitude):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
    def __str__(self):
        return f"City: {self.name} ({self.latitude}, {self.longitude})"
    @staticmethod
    def distance(city1, city2):
        ov_latitude = abs(city1.latitude - city2.latitude)
        ov_longitude = abs(city1.longitude - city2.longitude)
        dist = ov_latitude + ov_longitude
        return round(dist, 2)
    @classmethod
    def from_string(cls, data):
        data = re.split(r"[,:]", data)
        city, latitude, longitude = data
        return cls(city, float(latitude), float(longitude))

city1 = City("Berlin", 52.52, 13.4)
city2 = City("Paris", 48.85, 2.35)
print(city1)
print(city2)
print(f"Distance: {City.distance(city1, city2)}")

"""2. Создание объекта из строки
Доработайте класс City.
● Добавьте метод from_string(data), который создаёт объект из строки вида "Rome:41.89,12.51".
● Проверьте создание нового объекта через этот метод и выведите его.
Пример вывода:
City: Rome (41.89, 12.51)"""

city3 = City.from_string("Rome:41.89,12.51")
print(city3)

"""1. Счётчик экземпляров
Создайте класс User, представляющий пользователя.
● При создании должны указываться логин (username) и пароль (password).
● У класса должно быть поле total_users, хранящее общее количество
созданных пользователей.
● При каждом создании нового объекта User, счётчик должен увеличиваться.
● Добавьте метод get_total(), возвращающий количество пользователей.
● Проверьте, что счётчик работает.
Пример вывода:
Total users: 2"""

class User:
    total_users = 0
    def __init__(self, login: str, password: str):
        if not (isinstance(login, str) and isinstance(password, str)):
            raise TypeError("Attributes must be str only!!")
        if len(login) == 0:
            raise ValueError("Login mustn't be empty!!")
        if len(password) < 5:
            raise ValueError(f"Invalid password: {password}\nMust be at least 5 symbols!!")
        self.login = login
        self.password = password
        User.total_users += 1
    @classmethod
    def get_total(cls):
        return cls.total_users
    def __str__(self):
        return f"User: {self.login}\nPassword: {self.password}"

user1 = User("Anton", "fish_sword_123")
user2 = User("Kirill", "88777abc")
print(f"Total users: {User.get_total()}")

"""2. Проверка данных пользователя
Доработайте класс User.
● Добавьте валидации полей при создании.
● Имя должно быть непустой строкой.
● Пароль должен быть строкой длиной не менее 5 символов.
● Если данные некорректны — выбрасывайте ValueError.
● Добавьте строковое представление объекта.
● Проверьте работу класса с разными значениями.

Пример вызова:
user1 = User("alice", "secret")
user2 = User("bob", "qwe")

Пример вывода:
User: alice
 ...
ValueError: Invalid password:
'qwe'.
"""

try:
    user1 = User("alice", "secret")
    print(user1)
except (TypeError, ValueError) as e:
    print(e)

try:
    user2 = User("bob", "qwe")
    print(user2)
except (TypeError, ValueError) as e:
    print(e)

