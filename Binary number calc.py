number = int(input("Введите число в десятичной системе: "))
rest = number
result = 0
while rest != 1:
    rest2 = rest
    rest = rest // 2
    rest2 = rest2 % 2
    if rest2 % 2 == 1:
        result = str(result) + str(rest2)
    else:
        result = str(result) + str(0)
else:
    result = str(result) + str(1)
    result = int(result[::-1]) // 10
    print(result)

print("\nТеперь давай переведём число обратно в десятичную систему!!")
print(f"Вот твоё число в бинарном виде: {result}, или можешь перевести любое новое число :)")
number = int(input("Введите число в двоичной системе: "))
buffer = 0
q = 1
while number != 0:
    result = number % 10 * q
    q = q * 2
    buffer = buffer + result
    number = number // 10
else:
    result = buffer
    print(result)

"Var II"

number = int(input("Введите число в десятичной системе: "))
rest = number
result = ""
while rest != 1:
    rest2 = rest
    rest = rest // 2
    rest2 = rest2 % 2
    if rest2 % 2 == 1:
        result = result + str(1)
    else:
        result = result + str(0)
else:
    result = str(result) + str(1)
    result = int(result[::-1])
    print(result)

print("""Перевод обратно в десятичную.
Или введи другое число в бинарном виде :).""")

x = input("Введите число: ")
multiplyer = 1
res = 0

for i in x[::-1]:
    if i == "1":
        i = int(i) * multiplyer
        res = res + i
    else:
        multiplyer *= 2
        continue
    multiplyer *= 2

print(f"Число в десятичной: {res}")