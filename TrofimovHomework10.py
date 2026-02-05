# Task I

"""Напишите программу, которая моделирует работу торгового автомата.
Автомат принимает только монеты номиналом 1, 2, 5, 10 и 50.
Программа должна запрашивать у пользователя общую стоимость покупки,
а затем отображать сколько монет каждого типа нужно потратить,
чтобы использовать минимальное количество монет для оплаты товара."""

price = int(input("Введите стоимость товара: "))
"Var I"
# coin50 = 0
# coin10 = 0
# coin5 = 0
# coin2 = 0
# coin1 = 0
#
# coin50 = price // 50
# price = price % 50
# coin10 = price // 10
# price = price % 10
# coin5 = price // 5
# price = price % 5
# coin2 = price // 2
# price = price % 2
# coin1 = price // 1
#
# print(f"Внесите монеты номиналом 50: {coin50}", end="\n")
# print(f"Внесите монеты номиналом 10: {coin10}", end="\n")
# print(f"Внесите монеты номиналом 5: {coin5}", end="\n")
# print(f"Внесите монеты номиналом 2: {coin2}", end="\n")
# print(f"Внесите монеты номиналом 1: {coin1}", end="\n")
"Var II"
coins = [50, 10, 5, 2, 1]

"Var II.1"
# for i in coins[::1]:
#     res = price // i
#     price = price % i
#     if i == 50:
#         coin50 = res
#     elif i == 10:
#         coin10 = res
#     elif i == 5:
#         coin5 = res
#     elif i == 2:
#         coin2 = res
#     else:
#         coin1 = res
#
# print(f"Внесите монеты номиналом 50: {coin50}", end="\n")
# print(f"Внесите монеты номиналом 10: {coin10}", end="\n")
# print(f"Внесите монеты номиналом 5: {coin5}", end="\n")
# print(f"Внесите монеты номиналом 2: {coin2}", end="\n")
# print(f"Внесите монеты номиналом 1: {coin1}", end="\n")

"Var II.2"
for i in coins[::1]:
    if price == 0:
        break
    res = price // i
    if res == 0:
        continue
    price = price % i
    print(f"Внесите монеты номиналом {i}: {res}", end="\n")

# Task II

"""Напишите программу, которая изменяет изначальный список
и возводит в квадрат только нечётные числа."""

numbers = [4, 9, 1, 7, 2, 5, 0, 3, 7, 1, 3]
first = str(numbers)
x = 0
for i in numbers:
    if i % 2:
        numbers[x] = i ** 2
        x = x + 1
    else:
        x = x + 1
        continue

print(f"Изначальный список: {first}", f"Измененный список: {numbers}", sep="\n\n")