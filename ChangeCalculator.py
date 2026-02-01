price = int(input("Введите стоимость товара: "))
quantity = int(input("Введите количество товара: "))
summe = int(input("Введите сумму оплаты: "))
result = summe - (price * quantity)
print("Сдача: " + str(result) + "рублей")

