# Task I

numbers = [1245.4435, -302.1403, 87459.99, -520.8265, 1450.001]
res = 0
for item in range(0, len(numbers)):
    if numbers[item] > 0:
        res = res + numbers[item]

print(f"Сумма положительных чисел: ${res:,.2f}")

# Task II

data_list = [
 "John 23 12345.678",
 "Alice 30 200.50",
 "Bob 35 15000.3",
 "Charlie 40 500.75"
]

buffer = []

for item in range(0, len(data_list)):
    buffer = data_list[item].split()
    name = buffer[0]
    age = buffer[1]
    summe = float(buffer[2])
    print("Имя: {0:<10} | Возраст: {1:<3} | Баланс: {2:>10,.2f}".format(name, age, summe))
