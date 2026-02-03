# text1 = "AB"
# text2 = "12"
#
# counter = 0
#
# for i in text1:
#     print("****************")
#     for j in text2:
#         print(i, j)
#         counter = counter + 1
# print(counter)

# # "Show me Time"
# "Var I"
# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             if minutes < 10 and seconds < 10:
#                 print(hours, ":0", minutes, ":0", seconds, sep="")
#             elif minutes < 10 and seconds > 10:
#                 print(hours, ":0", minutes, ":", seconds, sep="")
#             elif minutes > 10 and seconds < 10:
#                 print(hours, ":", minutes, ":0", seconds, sep="")
#             else:
#                 if seconds == 10 and minutes < 10:
#                     print(hours, ":0", minutes, ":", seconds, sep="")
#                 if seconds < 10 and minutes == 10:
#                     print(hours, ":", minutes, ":0", seconds, sep="")
#                 else:
#                     print(hours, ":", minutes, ":", seconds, sep="")

# "Var II"
# for hours in range(24):
#     for minutes in range(60):
#         for seconds in range(60):
#             if minutes < 10 and seconds < 10:
#                 print(hours, ":0", minutes, ":0", seconds, sep="")
#             elif minutes < 10 and seconds >= 10:
#                 print(hours, ":0", minutes, ":", seconds, sep="")
#             elif minutes >= 10 and seconds < 10:
#                 print(hours, ":", minutes, ":0", seconds, sep="")
#             else:
#                 print(hours, ":", minutes, ":", seconds, sep="")


# "Время только до конца дня :DD"
#
# print("""Отсчитываем 3 часа. Время закончится или по истечении 3-х часов
# или когда закончится текущий день""")
# current_time = int(input("Введите текущий час: "))
#
# end_time = current_time + 3
#
# while current_time < end_time and current_time < 24:
#     for minutes in range(60):
#         if minutes < 10:
#             print(current_time, ":0", minutes, sep="")
#         else:
#             print(current_time, ":", minutes, sep="")
#     current_time = current_time + 1

# Test
for i in range(3):
    for j in range(3):
        print(i + j, end=" ")