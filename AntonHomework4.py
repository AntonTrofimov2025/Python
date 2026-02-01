# Task 1
#
# print("""Введите логическое число, где 0 - Ложь, всё остальное - Истина.
# И получите результат :)""")
#
# first_digit = bool(int(input("Введите первое число: ")))
# second_digit = bool(int(input("Введите первое число: ")))
#
# num1 = first_digit
# num2 = second_digit
#
# print("first_digit", "second_digit", "    and")
# print("   ", num1, "      ", num2, "     ", num1 and num2)
# print("     or", "    not(first digit)")
# print("   ", num1 or num2, "        ", not num1)
#
# num3 = first_digit == second_digit
# num4 = first_digit != second_digit
#
# print("Same digits?", "   Not same?")
# print("   ", num3, "       ", num4)
#
# Task 2

print("""Проверьте, открыто ли окно и горит ли свет в комнате.
Ответьте командами 1(YES) or 0(NO)""")

light = input("Is the light on in the room?: ")
light = bool(int(light)) == True
window = input("Is the room's window open?: ")
window = bool(int(window)) == True
both = window and light
least_one = light or window

print("Light on?", "Window open?", "Both conditions met?", "At least one?")
print(" ", light, "     ", window, "          ", both, "          ", least_one)

# Task 3
#
# print("Рассчитай мне стоимость потребленного трафика",
#       "мобильного интернета по моему тарифу.", sep = '\n')
# print("""Базовая стоимость: 30 евро.
# Каждый мегабайт интернета сверх 500 МБ стоит 0.2 евро""")
#
# used_mb = int(input("Введите использованные мегабайты: "))
#
# base_price = 30
# exceeding_tariff = (used_mb > 500) * (used_mb - 500) * 0.2
# # Если условие (used_mb > 500) больше 500, то будет True(1), если меньше - False(0)
# """Здесь получается используется условие, которое срабатывает если
# использованные мегабайты превышают 500, тогда происходит рассчет по формуле
# В ином случае будет False, т.е. 0, а умножение на 0 дает 0,
# что позволяет избежать ошибок расчёта при вводе , например, числа 450."""
# total_price = base_price + exceeding_tariff
#
# print("Общая стоимость: ", total_price)