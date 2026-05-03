"Фабрика функций расчёта НДС"
"""Создайте функцию vat_calculator(rate), которая принимает ставку НДС и возвращает другую функцию.
Полученная функция должна принимать сумму и возвращать цену с учётом НДС по переданной ставке.
Пример вызова:
print(vat_20(100))
print(vat_10(200))
Пример вывода:
120.0
220.0"""

def vat_calculator(rate):
    def your_summe(summ):
        return round(summ * (rate / 100 + 1), 1)
    return your_summe

vat_20 = vat_calculator(20)
vat_10 = vat_calculator(10)

print(vat_20(100))
print(vat_10(200))

"Калькулятор скидок по категориям"
"""Создайте функцию, которая возвращает другую функцию для расчёта скидки.
Внешняя функция принимает словарь скидок, например {"food": 0.1} — 10% на еду.
Если категория не найдена — цена не меняется.

Пример вызова:
discounts = {"food": 0.1, "clothes": 0.2}
print(friday_discount("food", 100))
print(friday_discount("clothes", 250))
print(friday_discount("electronics", 500))

Пример вывода:
90.0
200.0
500"""

discounts = {"food": 0.1, "clothes": 0.2}

def disc_cat(your_categories):
    def disc_calc(product, summe):
        # if product not in your_categories:
        #     return summe
        discount = your_categories.get(product, 0)
        return summe * (1 - discount)
    return disc_calc

friday_discount = disc_cat(discounts)

print(friday_discount("food", 100))
print(friday_discount("clothes", 250))
print(friday_discount("electronics", 500))

"Настроенная функция вывода"
"""Создайте функцию custom_printer(sep, end), которая возвращает новую функцию печати,
использующую указанные значения sep и end по умолчанию.

Пример вызова:
printer = custom_printer(sep=' | ', end=' -->\n')
printer('Hello', 'World')
printer('Python', 'Java', 'C++')

Пример вывода:
Hello | World -->
Python | Java | C++ --> """

def custom_printer(sep, end):
    def your_text(*text):
        text = sep.join(str(word) for word in text)
        text += end
        print(text)
    return your_text

printer = custom_printer(sep=' | ', end=' -->\n')
printer('Hello', 'World')
printer('Python', 'Java', 'C++')

"Нумерация вызовов функции"
"""Создайте декоратор call_counter, который выводит имя и номер вызова функции каждый раз, когда она
вызывается.
Номер должен увеличиваться при каждом вызове.

Пример декорируемой функции:
def greet():
    print("Привет!")
    
Пример вывода:
Вызов функции 'greet' №1:
Привет!
Вызов функции 'greet' №2:
Привет!
Вызов функции 'greet' №3:
Привет!
"""

def call_decorator(func):
    count = 0
    def wrapper():
        nonlocal count
        count += 1
        print(f"Вызов функции '{func.__name__}' №{count}:")
        return func()
    return wrapper

@call_decorator
def greet():
    print("Привет!")

greet()
greet()
greet()

"1. Фабрика функций округления"
"""Создайте функцию make_rounder(), которая принимает количество знаков для
округления и возвращает другую функцию.
Полученная функция должна принимать число и возвращать его, округлённое до
указанного ранее количества знаков после запятой.

Пример вызова:
print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

Пример вывода:
3.14
2.72
10.0"""

def make_rounder(rounding_number):
    def number_receiver(your_num):
        return round(your_num, rounding_number)
    return number_receiver

round2 = make_rounder(2)
round0 = make_rounder(0)

print(round2(3.14159))
print(round2(2.71828))
print(round0(9.999))

"2. Расширяемый логгер событий"
"""Создайте функцию, которая возвращает вложенный логгер событий.
Каждый вызов логгера должен сохранять событие с текущим временем (если оно
передано) и возвращать весь список событий.

Пример вызова:
log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")
for event in log():
    print(event)
 
Пример вывода:
Загрузка данных: 2025-03-24 14:06:29
Обработка завершена: 2025-03-24 14:06:29
Сохранение файла: 2025-03-24 14:06:29
"""

from datetime import datetime

def logger():
    res = []
    check_names = set()
    def your_event(event_name=None):
        if event_name not in check_names and event_name is not None:
            res.append(f'{event_name}: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
            check_names.add(event_name)
        return res
    return your_event

log = logger()

log("Загрузка данных")
log("Обработка завершена")
log("Сохранение файла")
for event in log():
    print(event)

"3. Рамка вокруг вывода"
"""Создайте декоратор frame, который оборачивает результат функции рамкой из 50 символов -, выводя по
строке до и после вызова функции.

Пример декорируемой функции:
def say_hello():
    print("Привет, игрок!")
    
Пример вывода:
--------------------------------------------------
Привет, игрок!
--------------------------------------------------"""

def frame(func):
    def wrapper():
        print(50 * '-')
        func()
        print(50 * '-')
    return wrapper

# @frame
def say_hello():
    print("Привет, игрок!")

hello_with_hyphen = frame(say_hello)

hello_with_hyphen()

# say_hello()

