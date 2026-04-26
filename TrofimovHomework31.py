"Проверка пароля"
"""Реализуйте программу, которая должна проверить, соответствует ли введённый пароль следующим требованиям:
● Минимум 8 символов
● Есть хотя бы одна заглавная буква
● Есть хотя бы одна строчная буква
● Есть хотя бы одна цифра
Пример вывода:
Введите пароль: Pass1234
Пароль надёжен.
---
Введите пароль: k2n6bd7
Пароль не соответствует требованиям.
"""
from string import ascii_uppercase, ascii_lowercase, digits

def pass_validation(your_pass_bitte: str) -> bool:
    if len(your_pass_bitte) < 8:
        return False
    if not (any(l in ascii_uppercase for l in your_pass_bitte)
            and any(l in ascii_lowercase for l in your_pass_bitte)
            and any(l in digits for l in your_pass_bitte)):
        return False
    return True

while True:
    give_your_pass = input("Введите пароль (Выход: q): ")
    if give_your_pass.lower().strip() == "q":
        break
    if pass_validation(give_your_pass):
        print("Пароль надёжен.")
    else:
        print("Пароль не соответствует требованиям.")

"Извлечение IP-адресов"
"""Программа должна найти все IPv4-адреса в строке.
IPv4-адрес состоит из четырёх чисел от 0 до 255, разделённых точками.
Данные:
text = "Server1: 192.168.1.1, Server2: 10.0.0.254, Invalid: 999.123.456.78"
Пример вывода:
192.168.1.1
10.0.0.254"""
import re

text = "Server1: 192.168.1.1, Server2: 10.0.0.254, Invalid: 999.123.456.78"

searching = re.finditer(r"\b\d+\.\d+\.\d+\.\d+\b", text)

for ip in searching:
    if all(0 <= int(number) <= 255 for number in ip.group().split(".")):
        print(ip.group())

"""1. Извлечение дат
Реализуйте программу, которая должна:
● Найти в тексте все даты в форматах DD/MM/YYYY, DD-MM-YYYY и DD.MM.YYYY.

Пример вывода:
15/03/2025
01.12.2024
09-09-2023
28/02/2022
"""
import re

text = """The events N 123456 happened on
15/03/2025, 01.12.2024 and 09-09-2023.
Deadline: 28/02/2022."""

match = re.finditer(r"\d{2}[./-]\d{2}[./-]\d{4}", text)

for date in match:
    print(date.group())

"""2. Разделение списка тегов
Реализуйте программу, которая должна:
● Прочитать строку с тегами, введёнными пользователем.
● Разделить её на отдельные теги, независимо от того, чем они были разделены (запятые, точки с
запятой, слэши или пробелы).
● Удалить лишние пробелы и пустые значения.

Пример вывода:
['python', 'data-science', 'machine-learning', 'AI', 'neural-networks']
"""
import re

tag_input = "python, data-science / machine-learning; AI neural-networks"

"Var II"
processing = re.split(r"[,./; ]+", tag_input)

print(processing)

"Var I"
processing = re.sub(r"\s*[,/.; ]\s*", " ", tag_input).split()

print(processing)