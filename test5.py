# print("Введите свои данные для анкеты:")
# name = input("Введите имя: ")
# age = input("Введите возраст: ")
# colour = input("Введите любимый цвет: ")
# print("Меня зовут ", name,", мне", age," лет, и мой любимый цвет — ", colour)
#
# print("Она сказала: \"Привет!\"")
# print("Она сказала: \"Привет!\"")
# print("Она сказала: \"Привет!\"")
#
#
# print("Она сказала: \"Привет!\" \n" * 3)
#
# print("Список дел: \n", "\tУчеба\n", "\tУборка\n", "\tСпорт\n")

distance = int(input("Введите расстояние (в км): "))
speed = int(input("Введите среднюю скорость (в км/ч): "))

travel_time = int(distance / speed * 60)
hours = travel_time // 60
minutes = travel_time % 60

print("Время в пути: ", hours,"часа и ", minutes, "минут")