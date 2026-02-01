#task 1
# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter another number: "))
# num3 = int(input("Enter another number: "))
# print("Упорядочены" if (num3 > num2 and num3 > num1) and (num2 > num1) else "Не упорядочены")

# first = int(input('Введите первое число: '))
# second = int(input('Введите второе число: '))
# third = int(input('Введите третье число: '))
# numbers = [first, second, third]
#
# if numbers == sorted(numbers):
#     print('Числа отсортированы по порядку')
# else:
#     print('Числа не по порядку')

# #task2
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# if num1 == num2:
#     print('Числа равны')
# elif num1 > num2:
#     print(num1)
# else:
#     print(num2)

# #task3.1
# num1 = int(input("Введите число: "))
# if num1 % 2:
#     print('Нечетное')
# else:
#     print('Четное')
# #task3.2
# num2 = int(input("Введите число: "))
# print('Нечетное' if num2 % 2 else 'Четное')

# #task4
# age = int(input("Введите ваш возраст: "))
# if age < 12:
#     print('Вы Ребенок')
# elif age < 18:
#     print('Вы Подросток')
# elif age < 60:
#     print('Вы Взрослый')
# else:
#     print('Вы Пожилой')

# #task5
# num1 = int(input('Введите первую сторону: '))
# num2 = int(input('Введите вторую сторону: '))
# num3 = int(input('Введите третее число: '))
# if num1 + num2 > num3 or num2 + num3 > num1 or num1 + num3 > num2:
#     print('Такой треугольник может существовать')

# #task6
# text = str(input('Введите строку: '))
# print('Строка пуста' if text == "" else "Строка заполнена")

# #task7
# num1 = int(input('Введите первую кординату: '))
# num2 = int(input('Введите вторую кодинату: '))
# if num1 > 0 and num2 > 0:
#     print('Первый квадрант')
# elif num1 < 0 and num2 > 0:
#     print('Второй квадрант')
# elif num1 < 0 and num2 < 0:
#     print('Третий квадрант')
# elif num1 > 0 and num2 < 0:
#     print('Четвертый квадрант')
# else:
#     print('находится на одной из осей' )

# #task8.1
# num1 = int(input('Введите часы: '))
# num2 = int(input('Введите минуты: '))
# if num1 < 24:
#     print('Корректное время')
# elif num2 < 59:
#     print('Корректное время')
# else:
#     print('Некоректное время')
# #task8.2
# num1 = int(input('Введите часы: '))
# num2 = int(input('Введите минуты: '))
# if num1 < 24 and num2 < 60:
#     print('Корректное время')
# else:
#     print('Некоректное время')
# #task8.3
# hours = int(input('Введите часы: '))
# minutes = int(input('Введите минуты: '))
# seconds = int(input('Введите секунды: '))
#
# if hours > 24 or minutes > 60 or seconds > 60:
#     print('Некорректное время.')
# else:
#     print('Корректное время.')

#task9