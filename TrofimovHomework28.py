"1. Фильтрация по ключевому слову"
"""Напишите программу, которая помогает планировать дела. Программа должна бесконечно выводить план на
следующий день недели, пока пользователь нажимает 'Enter'.

Пример ввода:
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана:
Tuesday: Meeting, Work, Study Python
...
Нажмите 'Enter' для получения плана:
Sunday: Family time, Rest
Нажмите 'Enter' для получения плана:
Monday: Gym, Work, Read book
Нажмите 'Enter' для получения плана: q"""

# Данные:
# Расписание дел на неделю
weekly_schedule = {
 "Monday": ["Gym", "Work", "Read book"],
 "Tuesday": ["Meeting", "Work", "Study Python"],
 "Wednesday": ["Shopping", "Work", "Watch movie"],
 "Thursday": ["Work", "Call parents", "Play guitar"],
 "Friday": ["Work", "Dinner with friends"],
 "Saturday": ["Hiking", "Rest"],
 "Sunday": ["Family time", "Rest"]}

import itertools
iterator = itertools.cycle(weekly_schedule.items())

while True:
    x = input("Нажмите 'Enter' для получения плана: ")
    if x.lower().strip() == "q":
        break
    day, schedule = iterator.__next__()
    print(f"{day}: {', '.join(schedule)}")

"2. Объединение списков продуктов"
"""Напишите функцию, которая принимает несколько списков с названиями продуктов и возвращает генератор,
содержащий все продукты в нижнем регистре. Выведите содержимое генератора.

Пример вывода:
apple
banana
orange
carrot
tomato
cucumber
milk
cheese
yogurt
"""

fruits = ["Apple", "Banana",
"Orange"]
vegetables = ["Carrot", "Tomato",
"Cucumber"]
dairy = ["Milk", "Cheese",
"Yogurt"]

import itertools

def food_chain(*your_foods):
    iterator = itertools.chain(*your_foods)
    return iterator

print("\n".join(item.lower() for item in food_chain(fruits, vegetables, dairy)))

"3. Комбинации одежды"
"""Напишите функцию, которая принимает списки типов одежды, цветов и размеров, а затем генерирует все
возможные комбинации в формате "Clothe - Color - Size".

Пример вывода:
T-shirt - Red - S
T-shirt - Red - M
T-shirt - Red - L
T-shirt - Blue - S
...
Jacket - Black - L
"""

clothes = ["T-shirt", "Jeans",
"Jacket"]
colors = ["Red", "Blue", "Black"]
sizes = ["S", "M", "L"]

import itertools

def all_combos(*your_data):
    iterator = itertools.product(*your_data)
    return iterator

print(*(" - ".join(combo) for combo in all_combos(clothes, colors, sizes)), sep="\n")

"Генерация безопасных паролей"
"""Программа должна сгенерировать все возможные пароли длиной 4 символа, соблюдая следующие условия:
● Пароль должен содержать хотя бы одну заглавную букву, одну строчную букву и одну цифру.
● Символы не должны повторяться.
● Соседние символы не могут быть расположены подряд в таблице символов.
● Все подходящие пароли записываются в файл valid_passwords.txt

Данные:
from string import ascii_lowercase,
ascii_uppercase, digits

Пример данных в файле:
acA0
acA1
acA2
acA3
acA4
acA5
acA6
acA7
acA8
...
"""

from string import ascii_lowercase, ascii_uppercase, digits
import itertools

all_together = ascii_lowercase + ascii_uppercase + digits

def is_valid(password):
    has_low = any(c in ascii_lowercase for c in password)
    has_up = any(c in ascii_uppercase for c in password)
    has_dig = any(c in digits for c in password)
    if not (has_low and has_up and has_dig):
        return False
    if len(password) != len(set(password)):
        return False
    for i in range(len(password) - 1):
        if abs(ord(password[i]) - ord(password[i + 1])) == 1:
            return False
    return True

iterator = itertools.permutations(all_together, 4)

basket = []
pswd_counter = 0
for pswd in iterator:
    if is_valid(pswd):
        pswd = "".join(pswd) + "\n"
        basket.append(pswd)
        pswd_counter += 1
with open("valid_passwords.txt", "w", encoding="utf-8") as all_pswds:
    all_pswds.writelines(basket)
print(*basket)
print(f"all possible combinations: {pswd_counter}")