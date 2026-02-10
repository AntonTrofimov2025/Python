# Task I

text = "My number is 123-456-789"
res = ""

for i in text:
    if i.isdigit():
        res = res + "*"
    else:
        res = res + i

print(res)

# Task II

text = "Programming in python".lower()
buffer = ""

for i in range(0, len(text)):
    if text.count(text[i]) > 1 and text[i] not in buffer:
        times = text.count(text[i])
        print(f"Символ '{text[i]}' встречается {times} раз(а)")
        buffer = buffer + text[i]
    else:
        continue

# Task III

text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672.".split()
res = ""

# for i in text:
#     if i.isdigit() or i == "0.5":
#         b = str(float(i) * 10)
#         res = res + b + " "
#     else:
#         res = res + i + " "

for i in text:
    if i.isdigit() or i.replace(".", "", 1).isdigit():
        res = res + str(float(i) * 10) + " "
    else:
        res = res + i + " "

print(res)