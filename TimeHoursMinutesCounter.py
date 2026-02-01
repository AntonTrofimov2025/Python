distance = int(input("Введите расстояние (в км): "))
speed = int(input("Введите среднюю скорость (в км/ч): "))

travel_time = int(distance / speed * 60)
hours = travel_time // 60
minutes = travel_time % 60


print("Время в пути: ", hours, "часа и ", minutes, " минут")