print("Число Армстронга")
number = int(input("Введите число: "))
buffer = 0
buffer2 = ""

for i in range(1, number + 1):
    i = str(i)
    length = len(i)
    i = int(i)
    comp = i
    while i != 0:
        res = i % 10
        i = i // 10
        buffer = buffer + res ** length
    if buffer == comp:
        buffer = str(buffer)
        buffer2 = buffer2 + buffer + ", "
        buffer = int(buffer)
    buffer = 0

print(buffer2[0: len(buffer2) - 2])