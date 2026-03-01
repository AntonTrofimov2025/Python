# Task 1

"""Напишите программу, которая преобразует список оценок
по системе от 1 до 5 в текстовое представление.
Нужно сохранить в списках числовой результат и текстовое представление.
Где, 5 — "отлично", 3-4 — "хорошо", а 2 и ниже — "неудовлетворительно"."""

grades = [5, 3, 4, 2, 1, 5, 3]
# processed = []
#
# for grade in grades:
#     total = []
#     total.append(grade)
#     if grade == 5:
#         total.append('отлично')
#     elif grade > 2:
#         total.append('хорошо')
#     else:
#         total.append('неудовлетворительно')
#     processed.append(total)

processed = [[grade, 'отлично' if grade == 5 else ('хорошо' if grade > 2 else 'неудовлетворительно')]
             for grade in grades]

print(processed)

# Task 2

brackets = "([({}()){}])"
print(f"Скобки: {brackets}")
brackets = list(brackets)

"Version II"

for index in range(len(brackets) -1, -1, -1):
    if brackets and ord(brackets[index]) == ord(brackets[index - 1]) + 1 or brackets and ord(brackets[index]) == ord(brackets[index - 1]) + 2:
        brackets.pop(index)
        brackets.pop(index - 1)

if brackets:
    success = False

"First working version"
# right_bracket = len(brackets) - 1
# while brackets:
#     if ord(brackets[0]) == ord(brackets[right_bracket]) - 1 or ord(brackets[0]) == ord(brackets[right_bracket]) - 2:
#         brackets.pop(0)
#         brackets.pop()
#     for index in range(len(brackets) -1, -1, -1):
#         if brackets and ord(brackets[index]) == ord(brackets[index - 1]) + 1 or brackets and ord(brackets[index]) == ord(brackets[index - 1]) + 2:
#             brackets.pop(index)
#             brackets.pop(index - 1)
#     right_bracket = len(brackets) - 1
#     if brackets:
#         success = False
#         break

if not brackets:
    success = True

print(f"Валидны: {success}")

# Tasks from lesson

"""Напишите программу, которая принимает список строк и
печатает новый список, в котором содержатся только
строки длиной больше 3 символов в перевёрнутом виде."""

words = ["cat", "elephant", "dog", "bird",
"lion", "ant"]

# new_list = []
#
# for word in words:
#     if len(word) > 3:
#         new_list.append(word[::-1])

new_list = [word[:: -1] for word in words if len(word) > 3]

print(new_list)

"""Напишите программу, которая принимает двумерный
список (матрицу) и создает новый список, содержащий
суммы элементов каждой строки."""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# new_list = []
#
# # for raw in matrix:
#     new_list.append(sum(raw))

new_list = [sum(raw) for raw in matrix]

print(new_list)