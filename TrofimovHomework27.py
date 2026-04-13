"Подсчёт частоты слов в файле"
"""Напишите программу, которая подсчитывает, сколько раз каждое слово встречается в файле
(не учитывая регистр).
● Программа запрашивает имя файла и количество популярных слов для вывода.
● Если указанный файл не существует, программа должна вывести ошибку.
Используйте файл text.txt.

Пример ввода:
Введите имя файла: text.txt
Введите количество популярных слов: 3"""

# from collections import Counter
#
# words = ["Hello", "Hello", "Hello", "World", "WoRLD"]
#
# res = Counter(w.lower() for w in words)
# print(res)

from collections import Counter
file_name = input("Введите имя файла: ")
how_many_words = int(input("Введите количество популярных слов: "))

try:
    with open(file_name, "r", encoding="utf-8") as file:
        words = file.read().split()
        res = Counter(w.lower() for w in words).most_common(how_many_words)
        print("Популярные слова:")
        for key, value in res:
            print(f"{key}: {value}")
except FileNotFoundError:
    print("Указанный файл не существует")

"Удаление пустых строк"
"""Напишите программу, которая удаляет пустые строки из указанного пользователем файла и
записывает результат в новый файл.
Имя нового файла формируется автоматически по шаблону <oldname>_cleaned.txt.
Если указанный файл не существует, программа должна вывести ошибку.
Используйте файл tasks.txt.

Пример ввода:
Введите имя файла: tasks.txt

Пример вывода:
Пустые строки удалены, сохранено в
tasks_cleaned.txt."""

file_name = input("Введите имя файла: ")
new_file_name = file_name.replace(".txt", "_cleaned.txt")

try:
    with (open(file_name, "r", encoding="utf-8") as old,
        open(new_file_name, "w", encoding="utf-8") as new):
        for line in old:
            if line.strip():
                new.write(line)
        print(f"Пустые строки удалены, сохранено в {new_file_name}.")
except FileNotFoundError:
    print("Указанный файл не существует")

"Файлы с заданным расширением"
"""Напишите программу, которая:
● Принимает путь к директории и расширение файлов через
аргументы командной строки.
● Ищет файлы с указанным расширением в указанной
директории.
● Выводит список найденных файлов

Пример запуска
python script.py /home/user/projects .py

Пример вывода
Найденные файлы в директории '/home/user/projects':
script.py, test.py, main.py"""

import os
import sys

if len(sys.argv) != 3:
    print("Использование: python TrofimovHomework27.py <Путь> <Расширение>")
    sys.exit(1)

path = sys.argv[1]
extension = sys.argv[2]

if os.path.isdir(path):
    print(f"Найденные файлы в директории '{path}': ")
    res = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                res.append(file)
    print(", ".join(res))
else:
    print("Указанная директория не существует")
    sys.exit(1)

# Task I
"Фильтрация по ключевому слову"
"""Напишите программу, которая ищет в файле все строки, содержащие указанное пользователем слово, и
сохраняет их в новый файл.
● Имя нового файла формируется как <keyword>_<original_filename>.
● Если файл не существует, программа должна вывести ошибку.
● Если совпадения не найдены, новый файл не создаётся.
Используйте файл system_log.txt.

Пример ввода:
Введите имя файла для поиска: system_log.txt
Введите ключевое слово: error

Пример вывода:
Строки, содержащие 'error',
сохранены в error_system_log.txt."""

file_name = input("Введите имя файла для поиска: ")
key_word = input("Введите ключевое слово: ")
changed = key_word + "_" + file_name

try:
    with open(file_name, "r", encoding="utf-8") as old:
        lines_found = [line for line in old if key_word in line]
        if lines_found:
            with open(changed, "x", encoding="utf-8") as new:
                new.writelines(lines_found)
            print(f"Строки, содержащие '{key_word}', сохранены в {changed}.")
        else:
            print("Ключевое слово в строках не найдено.")
except FileNotFoundError:
    print("Ошибка: Указанный файл не существует")
except FileExistsError:
    print("Ошибка создания нового файла: Файл уже существует")

# Task II
"Поиск и удаление дубликатов"
"""Напишите программу, которая удаляет дублирующиеся строки из файла и сохраняет результат в новый файл.
● Имя нового файла формируется как unique_<original_filename>.
● Если файл не существует, программа должна вывести ошибку.
● Исходный порядок строк должен сохраниться.
● Если в файле нет дубликатов, создаётся точная копия файла.
Используйте файл movies_to_watch.txt.

Пример ввода:
Введите имя файла: movies_to_watch.txt

Пример вывода:
Дубликаты удалены. Уникальные
строки сохранены в
unique_movies_to_watch.txt."""

file_name = input("Введите имя файла: ")
new_file_name = "unique_" + file_name

try:
    with (open(file_name, "r", encoding="utf-8") as original,
        open(new_file_name, "x", encoding="utf-8") as unique):
        basket = []
        for line in original:
            if line not in basket:
                basket.append(line)
        unique.writelines(basket)
        print(f"Дубликаты удалены. Уникальные строки сохранены в {new_file_name}.")

except FileNotFoundError:
    print("Ошибка: Указанный файл не существует")
except FileExistsError:
    print("Ошибка создания нового файла: Файл уже существует")