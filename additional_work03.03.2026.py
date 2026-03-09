"""1. Преобразование регистров (Snake to Camel)
Напишите конвертер имен полей из базы данных (snake_case)
в формат JSON-ответа API (camelCase).

Вход: is_user_authenticated_and_active Выход: isUserAuthenticatedAndActive"""
"Var I"
x = "is_user_authenticated_and_active"
x = x.split("_")
i = 1

for item in x[1:]:
    x[i] = item.capitalize()
    i += 1

print("".join(x))

"Var II and III"
x = "is_user_authenticated_and_active".split("_")

for i, item in enumerate(x[1:], 1):
    x[i] = item.capitalize()

print("".join(x))

print("".join([x[0]] + [item.capitalize() for index, item in enumerate(x[1:], 1)]))

"""2. Детектор анаграмм (Query Optimization)
Проверьте, можно ли составить одну строку из другой
(полезно для поиска дубликатов в справочниках).

Вход: listen и silent Выход: True
"""
x = ["listen", "silent"]

"Var III"
print("Выход: ", end="")
print(*[sorted(x[index].lower()) == sorted(x[index + 1].lower()) for index in range(len(x) - 1)])

"Var II"
print(f"Выход: {sorted(x[0].lower()) == sorted(x[1].lower())}")

"Var I"
x[0] = sorted(x[0])
x[1] = sorted(x[1])

if x[0] == x[1]:
    print("Выход: True")
else:
    print("Выход: False")

"""3. Форматирование текста (Text Wrapper)
Реализуйте перенос строк для логгера: текст должен разбиваться на строки длиной не более
N символов, не разрывая слова.

Вход: "Python is awesome", лимит 10 Выход: '"'Python is\nawesome'"""

"Var II"
text = "Python is awesome"
limit = 10
res = []
counter = 0

for letter in text:
    res.append(letter)
    counter += 1
    if counter >= limit:
        for i in range(len(res) -1, -1, -1):
            if res[i] == " ":
                res[i] = "\n"
                counter = 0
                break

print("".join(res))

"Var I"
text = "Python is awesome"
limit = 10
res = []

for index, letter in enumerate(text):
    res.append(letter)
    if index == limit - 1 and letter == " ":
        res[index] = "\n"

print("".join(res))

"""4. Генератор URL-слагов (Slugify)
Напишите функцию, которая превращает заголовок статьи в валидный URL-фрагмент. Нужно заменить пробелы на дефисы, удалить знаки препинания и привести всё к нижнему регистру.

Вход: "Hello, World! Python 3.12 is out."
Выход: 'hello-world-python-3-12-is-out'"""

import string

"Var I"
inp = "Hello, World! Python 3.12 is out.".lower()

for sign in inp:
    if sign.isspace() or sign == ".":
        inp = inp.replace(sign, "-")
    if sign in string.punctuation:
        inp = inp.replace(sign, "")

print(inp[:-1])

"Var II"
inp = "Hello, World! Python 3.12 is out.".lower()
res = "".join("-" if sign.isspace() or sign == "." else "" if sign in string.punctuation else sign for sign in inp)[:-1]

print(res)

"""5. Выделение домена из Email
Для аналитики нужно вытащить только домен из почты.

Вход: "supporturgent@github.com"
Выход: 'github.com'"""

"Var II"
x = "supporturgent@github.com"

index = x.find("@")
if index == -1:
    print("not e-mail")
else:
    print(x[index + 1:])

"Var I"
x = "supporturgent@github.com"

if "@" in x:
    index = x.index("@")
    print(x[index + 1:])
else:
    print("not e-mail")

"Var 0"
x = "supporturgent@github.com"
index = 0

while x[index] != "@":
    index += 1

print(x[index + 1:])

"""6. Группировка логов по IP (Log Masking)
Есть строка лога. Нужно найти в ней IPv4 адрес и заменить его на [MASKED].
Помните, что в IPv4 четыре группы чисел (от 0 до 255), разделенных точками.

Вход: "User 192.168.1.1 logged in from 10.0.0.255"
Выход: 'User [MASKED] logged in from [MASKED]'"""

"Var I"
x = "User 192.168.1.1 logged in from 10.0.0.255.".split()

for index, element in enumerate(x):
    if "." in element:
        if "." in element[len(element) - 1]:
            element = element[:-1]
        if element.count(".") == 3:
            element = element.split(".")
            for digit in element:
                if digit.isdigit():
                    if int(digit) <= 255:
                        is_ipv4 = True
                else:
                    is_ipv4 = False
                    break
            if is_ipv4:
                x[index] = "[MASKED]"
            is_ipv4 = False

print(" ".join(x))

"Var II"
x = "User 192.168.1.1 logged in from 10.0.0.255.".split()

for index, element in enumerate(x):
    last_el = ""
    if "," in element:
        last_el = ","
    if "!" in element:
        last_el = "!"
    if "?" in element:
        last_el = "?"
    if "." not in element[-1::-1]:
        element = element[:-1]
        if element.count(".") != 3:
            element = element.split(".")
            for digit in element:
                if digit.isalpha():
                    break
    else:
         x[index] = "[MASKED]" + last_el

print(" ".join(x))

"""7. Распаковка «сжатых» строк (String Expansion)
Обратная задача сжатию. В некоторых API для экономии трафика передаются строки вида 3[a]2[bc].

Вход: "3[a]2[bc]d"
Выход: 'aaabcabcd'"""

"Var II"
x = "3[a]2[bc]d"
x = x.replace("[", " ").replace("]", " ").split()
mtplr = 1
res = ""

for index, letter in enumerate(x):
    if letter.isdigit():
        mtplr = int(letter)
    else:
        res += letter * mtplr
        mtplr = 1

print(res)

"Var I"
x = "3[a]2[bc]d"
x = x.replace("[", " ").replace("]", " ").split()
mtplr = 1

for index, letter in enumerate(x):
    if letter.isdigit():
        mtplr = int(letter)
        x[index] = ""
    else:
        x.pop(index)
        x.insert(index, letter * mtplr)
        mtplr = 1

print("".join(x))

"""8. Проверка на циклический сдвиг (Rotation Check)
Определите, является ли одна строка циклическим сдвигом другой.

Вход: "backend" и "endback"
Выход: True"""

x = "backend"
y = "endback"

print(True if y in x * 2 and len(x) == len(y) else False)

"""9. Поиск "Битых" JSON-ключей
Часто при миграциях ключи в JSON приходят с лишними пробелами
или невидимыми символами (типа \t или \n).
Напишите функцию, которая находит «грязные» ключи в строке-словаре
и возвращает список исправленных.

Вход: '{" user_id": 1, "email ": "a@b.com", " status\t": "active"}'
Выход: ["user_id", "email", "status"]"""
x = {" user_id": 1, "email ": "a@b.com", " status\t": "active"}
res = []
for key in x:
    res.append(key.strip())

print(res)

print([key.strip() for key in x])

"""10. Поиск подстроки с "Wildcard"
Реализуйте поиск подстроки, где символ ? в искомом шаблоне
может означать любую одну букву (аналог упрощенного LIKE в SQL).

Вход: текст "authentication", шаблон "t?nt"
Выход: True (так как есть "tent")"""
import string

x = "authentication".lower()
template = "t?en"
res = False

for item in string.ascii_lowercase:
    back = template
    template = template.replace("?", item)
    if template in x:
        res = True
        break
    template = back

print(res)

"""BONUS from Gemini
Задача «Детектор лжи в логах»:
Есть список событий: events = ["login", "logout", "login", "error", "login", "error"].
Нужно посчитать, сколько раз встретилось каждое слово, и выдать словарь вида
{'login': 3, 'logout': 1, 'error': 2}.
Попробуешь написать это через обычный цикл for и один пустой словарь?"""

events = ["login", "logout", "login", "error", "login", "error"]
res = []

for event in events:
    how_many = events.count(event)
    res.append((event, how_many))

print(dict(res))

events = ["login", "logout", "login", "error", "login", "error"]
res = {}

for event in events:
    if event in res:
        res[event] += 1
    else:
        res[event] = 1

print(res)

events = ["login", "logout", "login", "error", "login", "error"]
counts = {}

for index, event in enumerate(events):
    if event in counts:
        counts[event] += [index]
    else:
        counts[event] = [index]

print(counts)

"BONUS 2"
"""Вот тебе задачка:
У нас есть данные по продажам за три дня:
matrix = [[10, 20], [30, 40], [50, 60]]
Твоя цель:
Получить плоский список [10, 20, 30, 40, 50, 60].
Условие:
Сделай это двумя способами:
Классическим вложенным циклом for (один внутри другого).
Одной строкой через List Comprehension (вложенный генератор)."""

matrix = [[10, 20], [30, 40], [50, 60]]
res = []
for raw in matrix:
    for element in raw:
        res.append(element)
print(res)

print([element for raw in matrix for element in raw])