# Task I
"""Таблица умножения

Напишите программу, которая выводит таблицу умножения для чисел от 1 до n.
Где n это число, которое введет пользователь.
Оформите вывод так, чтобы столбцы были ровные (число ровно под числом)"""

number = int(input("Введите число: "))
multiplyer = 1

if number <= 50:
    for high in range(1, number + 1):
        for width in range(1, number + 1):
            if width * multiplyer >= 10:
                print(width * multiplyer, end="    ")
            elif width * multiplyer >= 100:
                print(width * multiplyer, end="  ")
            elif width * multiplyer >= 1000:
                print(width * multiplyer, end=" ")
            else:
                print(width * multiplyer, end="     ")
        print()
        multiplyer += 1
else:
    print("Зачем тебе такая таблица умножения? :)")

# Task II

"""Лестница чисел

Напишите программу, которая принимает число n и выводит "лестницу" из чисел.
Каждая строка лестницы содержит числа от 1 до номера строки."""

ladder = int(input("Введите число: "))

for high in range(1, ladder + 1):
    for width in range(1, high + 1):
        print(width, end=" ")
    print()

# Task III

"""Удаление всех повторяющихся символов

Напишите программу, которая принимает строку и удаляет из неё
все повторяющиеся символы, сохраняя только первые их вхождения."""

string = input("Введите строку: ")
buffer = ""

for i in range(len(string)):
    if string[i] in buffer:
        continue
    else:
        print(string[i], end="")
        buffer = buffer + string[i]
    i += 1

# Bonus

for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            if minutes < 10 and seconds < 10:
                print(hours, ":0", minutes, ":0", seconds, sep="")
            elif minutes < 10 and seconds >= 10:
                print(hours, ":0", minutes, ":", seconds, sep="")
            elif minutes >= 10 and seconds < 10:
                print(hours, ":", minutes, ":0", seconds, sep="")
            else:
                print(hours, ":", minutes, ":", seconds, sep="")