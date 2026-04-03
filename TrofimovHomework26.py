"Определение типа объекта"
"""Напишите программу, которая:
● Запрашивает у пользователя путь.
● Определяет, является ли путь файлом,
папкой или он не существует.
Пример ввода
Введите путь: example.txt
Пример вывода
example.txt — это файл."""

import os
path = input("Введите путь: ")

if os.path.exists(path):
    if os.path.isdir(path):
        print(f"{path} — это папка")
    elif os.path.isfile(path):
        print(f"{path} — это файл")
else:
    print("Указанный путь не существует")

"Файлы с заданным расширением"
"""Напишите программу, которая:
● Принимает путь к директории и расширение файлов
через аргументы командной строки.
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
    print("Использование: python TrofimovHomework26.py <Путь> <Расширение>")
    sys.exit(1)

directory = sys.argv[1]
extension = sys.argv[2]
if os.path.isdir(directory):
    for file in os.listdir(directory):
        if file.endswith(extension):
            print(f"- {file}")
else:
    print("Указанная директория не существует")
    sys.exit(1)

# Task I
"Список файлов и папок"
"""Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
● Отдельно список папок
● Отдельно список файлов
Пример запуска:
python script.py /home/user/documents
Пример вывода:
Содержимое директории '/home/user/documents':
Папки:
- folder1
- folder2
Файлы:
- file1.txt
- file2.txt
- notes.docx"""

"Var I"
import os
import sys

if len(sys.argv) != 2:
    print("Использование: python TrofimovHomework26.py <Путь>")
    sys.exit(1)

directory = sys.argv[1]

if os.path.isdir(directory):
    print(f"Содержимое директории '{directory}':")
    print("Папки:")
    for item in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, item)):
            print(f"- {item}")
    print("Файлы:")
    for item in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, item)):
            print(f"- {item}")
else:
    print("Указанная директория не существует")
    sys.exit(1)

"Var II"
import os
import sys

if len(sys.argv) != 2:
    print("Использование: python TrofimovHomework26.py <Путь>")
    sys.exit(1)

directory = sys.argv[1]

if os.path.isdir(directory):
    folders = [folder for folder in os.listdir(directory) if os.path.isdir(os.path.join(directory, folder))]
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    print(f"Содержимое директории '{directory}':")
    print("Папки:")
    for folder in folders:
        print(f"- {folder}")
    print("Файлы:")
    for file in files:
        print(f"- {file}")
else:
    print("Указанная директория не существует")
    sys.exit(1)

# Task II
"Поиск и удаление файлов с указанным расширением"
"""Напишите программу, которая
● Принимает путь к директории и расширение файлов через аргумент командной строки.
● Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
● Спрашивает у пользователя, хочет ли он удалить найденные файлы.
● Если пользователь подтверждает, удаляет их.
Пример запуска
python script.py /home/user/PycharmProjects/project1 .log
Пример вывода:
Найдены файлы с расширением '.log':
- logs/error.log
- logs/system.log
- logs/backup/old.log
- logs/backup/debug.log
Вы хотите удалить эти файлы? (y/n): y
Удаление завершено."""

import os
import sys

if len(sys.argv) != 3:
    print("Использование: python TrofimovHomework26.py <Путь> <Расширение>")
    sys.exit(1)

directory = sys.argv[1]
extension = sys.argv[2]

if os.path.isdir(directory):
    files_to_remove = []
    print(f"Найдены файлы с расширением '{extension}': ")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                files_to_remove.append(os.path.join(root, file))
                print(f"- {os.path.join(root, file)}")
    x = input("Вы хотите удалить эти файлы? (y / n): ")
    if x.lower().strip() == "y":
        for file in files_to_remove:
            os.remove(file)
        print("Удаление завершено")
    else:
        print("Файлы сохранены")
else:
    print("Указанная директория не существует")
    sys.exit(1)