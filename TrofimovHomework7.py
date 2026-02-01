# # Task 1
# # "Напишите программу, которая вычисляет сумму цифр введённого числа."
#
# num = int(input("Введите целое число: "))
#
# divider = 1
# digit = num % 10
#
# while divider < num:
#     divider = divider * 10
#     digit = digit + num // divider % 10
# else:
#     print(f"Сумма цифр: {digit}")

# Task 2
# "Var I"
# digit = int(input("Введите число: "))
#
# n = 1
# q = 1
# divider = 1
# num1 = 0
# num2 = 0
#
# while divider < digit:
#     divider = divider * 10
#     n = n + 1
# else:
#     n = n - 1
#     divider = divider // 10
#     count = (n / 2) - 1
#     while n > count and num1 == num2:
#         num1 = (digit // 10 ** (n - 1)) % 10
#         num2 = digit // q % 10
#         n = n - 1
#         q = q * 10
#         if n <= count:
#             print(f"Число {digit} является палиндромом.")
#             break
#     else:
#         print(f"Число {digit} не является палиндромом.")

# "Var II"
# number = input("Введите число: ")
# reverse_number = number[::-1]
# if number == reverse_number:
#     print(f"Число {number} является палиндромом.")
# else:
#     print(f"Число {number} не является палиндромом.")

"Var III"
number = int(input("Введите число: "))
initnumber = number
reverse_number = 0

while number != 0:
    digit = number % 10
    reverse_number = reverse_number * 10 + digit
    number = number // 10
else:
    if initnumber == reverse_number:
        print(f"Число {initnumber} является палиндромом.")
    else:
        print(f"Число {initnumber} не является палиндромом.")


# Task 3
import random
print("Угадайте число от 1 до 100. У вас 10 попыток!!! :))")
prediction = 0
count = 10

randdigit = random.randint(1, 100)

while count != 0:
    prediction = int(input("Ваше предположение: "))
    count = count - 1
    if prediction < randdigit and count != 0:
        print("Загаданное число больше вашего")
        print(f"Осталось: {count} попыток")
    elif prediction > randdigit and count != 0:
        print("Загаданное число меньше вашего")
        print(f"Осталось: {count} попыток")
    elif prediction == randdigit:
        print(f"Поздравляем! Вы угадали число: {randdigit}.")
        print(f"Вы угадали число за {10 - count} попытки.", "Отличный результат!" if count >= 7 else "Неплохо!! :)" if count >= 4 else "Ты старался! Молодцом :D")
        break
else:
    print("У Вас не осталось попыток, к сожалению :')")