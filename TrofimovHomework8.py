# Task I

charact = input("Введите символ: ")

charact = ord(charact)

print(f"Код Unicode: {charact}")

"Var I"
# if charact <= 127:
#     ascii = True
# else:
#     ascii = False
#
# if 128 <= charact <= 255:
#     ascii2 = True
# else:
#     ascii2 = False
"Var II"
if charact <= 127:
    ascii = True
    ascii2 = False
elif charact <= 255:
    ascii = False
    ascii2 = True
else:
    ascii = False
    ascii2 = False

print(f"ASCII символ: {ascii}")
print(f"Расширенный ASCII: {ascii2}")

# Task II

xstr = input("Введите строку: ")
init = int(input("Введите начальный индекс: "))
last = int(input("Введите конечный индекс: "))
newsym = ""

length = len(xstr)

if length < last:
    newsym = last - length
    newsym = "_" * newsym

xstr = xstr[init:last]

print(xstr + newsym)


# Task III

newstring = input("Введите строку: ")
checksym = input("Введите символ: ")

length = len(newstring)
right = length - 1
buffer = 0

while length != 0:
    if newstring[right] == checksym:
        buffer = buffer + 1
        right = right - 1
        length = length - 1
    else:
        right = right - 1
        length = length - 1

if buffer > 0:
    is_checksym = True
else:
    is_checksym = False

print(f"Символ {checksym} встречается? {"Да" if is_checksym == True else "Нет"}")
if buffer > 0:
    print(f"Символ {checksym} встречается {buffer} раз{"(а)" if buffer > 1 else ""}.")


# Task IV

print("Инвертирование строки без цифр")
xstring = input("Введите строку (например n52uFs6Inoh67ty8P): ")
count = len(xstring)
left = 0
buffer = ""

while count != 0:
    if xstring[left].isalpha():
        buffer = xstring[left] + buffer
        left = left + 1
        count = count - 1
    elif xstring[left].isdigit():
        left = left + 1
        count = count - 1

print(f"Результат: {buffer}")

# Bonus

x = input("Введите зашифрованный текст: ")
shift = int(input("Введите сдвиг: "))

count = len(x)
buffer = ""
right = count - 1

while count != 0:
    encoded_x = ord(x[right])
    encoded_x = encoded_x + shift
    decoded_x = chr(encoded_x)
    buffer = buffer + decoded_x
    count = count - 1
    right = right - 1

print(f"Расшифрованный текст: {buffer[::-1]}")

# Если ввести hellloy с шагом 4 то в выводе получим lippps} , забавная пасхалка :DD
# Случайно обнаружил :)