# # Task I
#
# number = "1 2 3 4 5"
# res = []
# number = number[::-1]
#
# for j in number:
#     if j.isdigit():
#         res.append(int(j))
#     else:
#         continue
#
# print(res)

# number = "1 2 3 4 5"
# res = 0
# number = list(number.split())
#
# for i in number:
#     i = int(i)
#     res = i + res

# # Task II

# number = "1 2 3 4 5"
#
# number = number[::-1]
# newlist = []
#
# print(number)
#
# for i in number.split():
#     newlist.append(int(i))
#
# print(newlist)
#
# digits = "1 2 3 4 5"
# res = []
# digits = digits.split()[::-1]
#
# for i in digits:
#     if i.isdigit:
#         i = int(i)
#         res.append(i)
#     else:
#         continue
#
# print(res)

# # Task III
#
# numbers = [-1, 8, 2, 0, -3, -9, -1, 10, 7, -4]
# odd = 0
# even = 0
#
# for i in numbers:
#     if i % 2:
#         odd = odd + i
#     else:
#         even = even + i
#
# print(f"Нечёт: {odd}, Чёт: {even}")

# Task IV
# "Var I"
# numbers = [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
# maxnum = 0
# index = 0
#
# for i in numbers:
#     if i > maxnum:
#         maxnum = i
#     else:
#         continue
#
# for j in numbers:
#     if j == maxnum:
#         break
#     else:
#         index = index + 1
#
# print(f"Biggest number: {maxnum}, its index: {index}")

# "Var II"
# numbers = [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
# maxnum = 0
# index = 0
#
# for i in range(0, len(numbers) - 1):
#     if numbers[i] > maxnum:
#         maxnum = numbers[i]
#         index = i
#     else:
#         continue
#
# print(f"Biggest number: {maxnum}, its index: {index}")

# Task V
# "Var I"
# numbers = [1, 2, 3, 4, 5]
# length = len(numbers)
# newlist = []
#
# for i in numbers[1:length - 1:2]:
#     newlist.append(i)
#     newlist.append(i - 1)
#
# newlist.append(numbers[length - 1])
#
# print(newlist)

# "Var II"
# numbers = [1, 2, 3, 4, 5]
# newlist = []
#
# for i in range(1, len(numbers) - 1):
#     if i in newlist:
#         continue
#     else:
#         newlist.append(numbers[i])
#         newlist.append(numbers[i - 1])
#
# newlist.append(numbers[len(numbers) - 1])
#
# print(newlist)


# # # Task VI
# "Var I"
# text = "apple 42 banana 3 100 orange"
# text = list(text.split())
# res = []
#
# for i in text:
#     if i.isdigit():
#         res.append(int(i))
#     else:
#         res.append(i.title())
#
# print(res)

# "Var II"
# text = "apple 42 banana 3 100 orange".title().split()
# res = []
#
# for i in text:
#     if i.isdigit():
#         i = int(i)
#         res.append(i)
#     else:
#         res.append(i)
#
# print(res)

# Task VII
"""Задача: Напишите программу, которая принимает строку и кодирует её с помощью
следующего правила: каждая последовательность одинаковых символов заменяется
на символ и количество его повторений. Например, строка aaaabbc превращается в
a4b2c1.
Пример вывода: Введите строку: aaaabbc
Закодированная строка: a4b2c1"""
# "Var I"
# string = "aaaabbc"
# res = ""
# num = 1
# buf = ""
#
# for i in string:
#     if i != buf:
#         res = res + str(num)
#         num = 1
#     if i not in res:
#         res = res + i
#         buf = i
#     else:
#         num = num + 1
#
# res = res + str(num)
#
# print(res[1:])

# "Var II"
# string = "aaaabbc"
# res = ""
#
# for i in range(0, len(string)):
#     if string[i] not in res:
#         res = res + string[i]
#         res = res + str(string.count(string[i]))
#     prev = string[i]
#
# print(res)
# --------------------------------------
# x = "aaaabbc"
# res = ""
#
# for i in range(0, len(x)):
#     if x[i] not in res:
#         res = res + x[i]
#         res = res + str(x.count(x[i]))
#
# print(res)

# # Task VIII

"""Задача: Напишите программу, которая проверяет, начинается ли строка с буквы,
содержит ли в себе символ @, и заканчивается ли на .com или .de.
Пример вывода: Введите email: user@example.com Корректный формат? True"""

# x = "user@example.com"
x = "antonio2026@gmail.de"

if x[0].isalpha():
    firstalpha = True
else:
    firstalpha = False

if "@" in x:
    at = True
else:
    at = False

# if ".com" in x[-4:] or ".de" in x[-3:]:
if x.endswith(".com") or x.endswith(".de"):
    endcomde = True
else:
    endcomde = False

iscorrect = firstalpha and at and endcomde
print(f"Your email: {x}, Correct?: {iscorrect}")

# # Task IX
# x = "My number is 123-456-789"
# res = ""
#
# for i in x:
#     if i.isdigit():
#         res = res + "*"
#     else:
#         res = res + i
#
# print(res)

# # Task X
# """Задача: Напишите программу, которая разворачивает каждое слово в строке,
# сохраняя их порядок.
# Пример вывода: Введите строку: Python is fun
# Результат: nohtyP si nuf
# """
# x = "Python is fun"
# buf = x.split()
# res = ""
#
# for i in buf:
#     res = res + i[::-1] + " "
#
# print(res[0: len(res) - 1])

# # Task XI
# """Задача: Напишите программу, которая подсчитывает количество букв, цифр и
# пробелов в строке. Также выведите количество остальных символов.
# Пример вывода: Введите строку: Python 3.12 is awesome!
# Буквы: 15 Цифры: 3 Пробелы: 3 Остальные символы: 2"""
# x = "Python 3.12 is awesome!"
# hmletters = 0
# hmdigits = 0
# spaces = 0
# other = 0
#
# for i in x:
#     if i.isalpha():
#         hmletters = hmletters + 1
#     elif i.isdigit():
#         hmdigits = hmdigits + 1
#     elif i.isspace():
#         spaces = spaces + 1
#     else:
#         other = other + 1
#
# print(f"Буквы: {hmletters} Цифры: {hmdigits} Пробелы: {spaces} Остальные символы: {other}")

# Task XII
"""Задача: Напишите программу, которая удаляет в строке лишние пробелы, оставляя
только по одному пробелу между словами.
Данные: text = " Hello, World! How are you? "
Пример вывода: Строка: ' Hello, World! How are you? ' Результат: 'Hello, World! How
are you?'"""
# "Var I"
# x = " Hello, World! How are you? "
# x = x.split()
# x =" ".join(x)
#
# print(x)
#
# "Var II"
# x = " Hello, World! How are you? "
# x = x.strip()
#
# print(x)

# "Var III"
# x = " Hello,          World!                How          are       you? "
# x = x.strip()
#
# while "  " in x:
#     x = x.replace("  ", " ")
#
# print(x)

# Task XIII

# Задача: Напишите программу, которая ищет подстроку в строке и выводит все
# индексы начала вхождения подстроки.
# Пример вывода: Строка: Banana bAnana baNAna Подстрока: ban Позиция: 0 Позиция:
# 7 Позиция: 14

x = "Banana bAnana baNAna"
x = x.lower()
substring = "ban"
index = x.find(substring)

while index != -1:
    print(index)
    index = x.find(substring, index + 1)

