# Пользователь вводит два числа. Проверьте, является ли одно из чисел четным, а
# другое - нечетным.

# # Variant I
# a, b = int(input("First digit even?: ")), int(input("Second digit odd?: "))
#
# is_even = bool(a % 2) == 0
# is_odd = bool(b % 2) != 0
# " Это здесь как not получается этот символ (!=),"
#
# print(is_even, is_odd)

# Variant II

a, b = int(input("First digit even?: ")), int(input("Second digit odd?: "))
# Нам нужно добиться чётких ответов на вопросы, где True - правда, False - неправда.
# Для эксперимента буду вводить 10 и 5 соответственно.
is_even = not bool(a % 2) # Здесь от 10 мы получаем 0, но чтоб было True ставим not.
is_odd = bool(b % 2)    # Здесь от 5 мы получаем 1, значит инвертировать цифру нам уже
                        # не нужно, она уже итак True.

print(is_even, is_odd)
