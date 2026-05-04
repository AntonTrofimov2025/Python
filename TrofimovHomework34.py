"1. Класс User"
"""Создайте класс User, который описывает пользователя.
● У каждого пользователя должно быть поля: username и email, а также счётчик входов login_count.
● Добавьте метод show_info(), который выводит имя и почту пользователя.
● Добавьте метод login(), который приветствует пользователя и фиксирует новый вход.
● Добавьте метод get_logins(), возвращающий текущее количество входов.
● Создайте пользователя, выполните несколько входов и выведите информацию.
Пример вывода:
------------------------------
Пользователь: alice
Почта: alice@example.com
------------------------------
alice вошёл в систему
alice вошёл в систему
Количество входов: 2"""

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.login_count = 0
    def show_info(self):
        print(f"Username: {self.username}\nE-Mail: {self.email}")
    def login(self):
        print(f"{self.username} has entered to the system")
        self.login_count += 1
    def get_logins(self):
        return self.login_count

new_user = User("alice", "alice@example.com")

new_user.show_info()
new_user.login()
new_user.login()
new_user.login()
print(f"Number of entrances: {new_user.get_logins()}")

"2. Класс Product"
"""Реализуйте класс Product, который описывает товар в магазине.
● Каждый объект должен хранить название (name) и цену (price).
● Добавьте метод apply_discount(), который уменьшает цену на заданный процент и выводит
информацию о размере примененной скидки.
● Добавьте метод info(), который выводит название и текущую цену товара.
● Проверьте работу класса: создайте товар, выведите его данные, примените скидку, затем снова
выведите информацию.
Пример вывода:
Название: Молоко
Цена: 120
Применяем скидку 25%
Новая цена: 90.0"""

class Product:
    def __init__(self, name: str, price: int | float):
        self.name = name
        self.price = price
    def apply_discount(self, disc_rate: int | float):
        self.price = self.price * (1 - disc_rate/100)
        print(f"Применяем скидку {disc_rate}%\nНовая цена: {self.price}")
    def info(self):
        print(f"Название: {self.name}\nЦена: {self.price}")

milk = Product("Молоко", 120)
milk.info()
milk.apply_discount(25)

"1. Класс Rectangle"
"""Создайте класс Rectangle, который описывает прямоугольник.
● У каждого объекта должны быть два поля: width и height.
● Добавьте метод get_area(), который возвращает площадь прямоугольника.
● Создайте объект прямоугольника с произвольными значениями.
● Выведите его площадь.
● Измените ширину и высоту.
● Выведите новую площадь.
Пример вывода:
Площадь: 20
Новая площадь: 35"""

class Rectangle:
    def __init__(self, width: int | float, height: int | float):
        if not (isinstance(width, int | float) and isinstance(height, int | float)):
            raise ValueError("Height and Width must be numbers!!")
        self.width = width
        self.height = height
    def get_area(self) -> int | float:
        S = self.width * self.height
        return S

my_rectangle = Rectangle(5, 4)
print(f"Площадь: {my_rectangle.get_area()}")
my_rectangle.width = 7
my_rectangle.height = 5
print(f"Новая площадь: {my_rectangle.get_area()}")

try:
    my_rectangle = Rectangle("5", 4)
    print(my_rectangle.get_area())
except ValueError as e:
    print(e)

"2. Класс Counter"
"""Реализуйте класс Counter, который представляет собой простой счётчик.
● Счётчик должен начинаться с нуля.
● Предусмотрите методы для увеличения и уменьшения значения на единицу, при
этом при каждой операции должно отображаться новое значение счётчика.
● Добавьте метод, возвращающий текущий результат.
● Проверьте работу счётчика, выполнив несколько операций.
Пример вывода:
Значение увеличено, текущее: 1
Значение увеличено, текущее: 2
Значение увеличено, текущее: 3
Значение уменьшено, текущее: 2
Текущее значение: 2"""

class Counter:
    def __init__(self, num: int=0):
        self.cur_count = num
    def increase(self):
        self.cur_count += 1
        print(f"Значение увеличено, текущее: {self.cur_count}")
    def decrease(self):
        self.cur_count -= 1
        print(f"Значение уменьшено, текущее: {self.cur_count}")
    def current_value(self):
        return self.cur_count

my_count = Counter()
my_count.increase()
my_count.increase()
my_count.increase()
my_count.decrease()
print(f"Текущее значение: {my_count.current_value()}")

