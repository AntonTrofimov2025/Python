"Поиск низких оценок за период"
"""Реализуйте программу, которая должна:
● Прочитать данные из файла grades.json.
● Реализовать функцию filter_low_scores(), которая:
○ Принимает минимальный проходной балл (threshold) и диапазон дат (start_date, end_date) в
формате дд-мм-гггг.
○ Возвращает все оценки ниже порога, полученные в заданный период.
○ Сохраняет отфильтрованные записи в файл filtered_low_scores.json.

Пример вызова:
filter_low_scores(70, "01-01-2025", "31-03-2025")

Пример вывода (filtered_low_scores.json):
[
 {"name": "Ethan", "subject": "History", "grade": 66, "date": "10-03-2025"},
 {"name": "Bob", "subject": "Literature", "grade": 68, "date": "22-01-2025"},
 {"name": "Ethan", "subject": "History", "grade": 62, "date": "25-02-2025"}
]
"""
import json
from datetime import datetime, timedelta

data = [
  {"name": "Bob", "subject": "Science", "grade": 86, "date": "06-09-2025"},
  {"name": "Diana", "subject": "Science", "grade": 85, "date": "31-01-2025"},
  {"name": "Bob", "subject": "Literature", "grade": 60, "date": "19-07-2025"},
  {"name": "Charlie", "subject": "Literature", "grade": 78, "date": "05-08-2025"},
  {"name": "Ethan", "subject": "Literature", "grade": 69, "date": "08-04-2025"},
  {"name": "Charlie", "subject": "Science", "grade": 63, "date": "24-10-2025"},
  {"name": "Ethan", "subject": "Math", "grade": 80, "date": "30-01-2025"},
  {"name": "Alice", "subject": "Physics", "grade": 90, "date": "15-09-2025"},
  {"name": "Ethan", "subject": "Science", "grade": 63, "date": "18-09-2025"},
  {"name": "Alice", "subject": "Science", "grade": 64, "date": "01-11-2025"},
  {"name": "Alice", "subject": "Science", "grade": 85, "date": "03-03-2025"},
  {"name": "Ethan", "subject": "Science", "grade": 97, "date": "01-11-2025"},
  {"name": "Alice", "subject": "Physics", "grade": 65, "date": "03-08-2025"},
  {"name": "Ethan", "subject": "Physics", "grade": 93, "date": "11-06-2025"},
  {"name": "Charlie", "subject": "Science", "grade": 80, "date": "03-05-2025"},
  {"name": "Charlie", "subject": "Literature", "grade": 68, "date": "10-12-2025"},
  {"name": "Charlie", "subject": "Literature", "grade": 80, "date": "07-02-2025"},
  {"name": "Alice", "subject": "Literature", "grade": 99, "date": "16-10-2025"},
  {"name": "Alice", "subject": "Math", "grade": 94, "date": "20-04-2025"},
  {"name": "Ethan", "subject": "History", "grade": 68, "date": "28-06-2025"},
  {"name": "Alice", "subject": "Science", "grade": 83, "date": "26-05-2025"},
  {"name": "Bob", "subject": "Literature", "grade": 94, "date": "27-12-2025"},
  {"name": "Charlie", "subject": "Physics", "grade": 93, "date": "05-01-2025"},
  {"name": "Ethan", "subject": "History", "grade": 66, "date": "10-03-2025"},
  {"name": "Charlie", "subject": "Math", "grade": 66, "date": "11-10-2025"},
  {"name": "Bob", "subject": "History", "grade": 78, "date": "06-11-2025"},
  {"name": "Bob", "subject": "History", "grade": 73, "date": "18-12-2025"},
  {"name": "Charlie", "subject": "Physics", "grade": 91, "date": "09-05-2025"},
  {"name": "Alice", "subject": "Math", "grade": 100, "date": "05-08-2025"},
  {"name": "Charlie", "subject": "Math", "grade": 60, "date": "20-06-2025"},
  {"name": "Bob", "subject": "History", "grade": 70, "date": "15-08-2025"},
  {"name": "Ethan", "subject": "Literature", "grade": 95, "date": "05-01-2025"},
  {"name": "Alice", "subject": "Math", "grade": 69, "date": "07-10-2025"},
  {"name": "Alice", "subject": "History", "grade": 97, "date": "10-10-2025"},
  {"name": "Bob", "subject": "Literature", "grade": 68, "date": "22-01-2025"},
  {"name": "Charlie", "subject": "History", "grade": 62, "date": "03-07-2025"},
  {"name": "Bob", "subject": "Science", "grade": 66, "date": "01-07-2025"},
  {"name": "Ethan", "subject": "Literature", "grade": 99, "date": "21-03-2025"},
  {"name": "Bob", "subject": "Science", "grade": 71, "date": "31-07-2025"},
  {"name": "Alice", "subject": "Science", "grade": 81, "date": "30-07-2025"},
  {"name": "Bob", "subject": "History", "grade": 70, "date": "26-12-2025"},
  {"name": "Alice", "subject": "Literature", "grade": 62, "date": "29-08-2025"},
  {"name": "Bob", "subject": "Science", "grade": 89, "date": "29-06-2025"},
  {"name": "Charlie", "subject": "Science", "grade": 74, "date": "13-01-2025"},
  {"name": "Bob", "subject": "Literature", "grade": 81, "date": "23-05-2025"},
  {"name": "Alice", "subject": "History", "grade": 82, "date": "25-11-2025"},
  {"name": "Ethan", "subject": "Literature", "grade": 94, "date": "19-06-2025"},
  {"name": "Alice", "subject": "Math", "grade": 76, "date": "02-04-2025"},
  {"name": "Ethan", "subject": "History", "grade": 62, "date": "25-02-2025"},
  {"name": "Ethan", "subject": "Literature", "grade": 82, "date": "10-06-2025"},
  {"name": "Diana", "subject": "Physics", "grade": 92, "date": "01-03-2025"},
  {"name": "Diana", "subject": "Physics", "grade": 72, "date": "11-05-2025"},
  {"name": "Alice", "subject": "Literature", "grade": 60, "date": "24-09-2025"},
  {"name": "Ethan", "subject": "Science", "grade": 83, "date": "09-08-2025"},
  {"name": "Alice", "subject": "History", "grade": 99, "date": "10-06-2025"},
  {"name": "Alice", "subject": "History", "grade": 92, "date": "08-06-2025"},
  {"name": "Diana", "subject": "History", "grade": 85, "date": "23-12-2025"},
  {"name": "Charlie", "subject": "Physics", "grade": 68, "date": "09-04-2025"},
  {"name": "Diana", "subject": "Literature", "grade": 71, "date": "12-11-2025"},
  {"name": "Ethan", "subject": "History", "grade": 85, "date": "08-10-2025"}
]

with open("grades.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

# # Example of Deserialization
# new_data = None
# try:
#     new_data = open("grades.json", "r")
#     res = json.load(new_data)
#     print(res)
# except FileNotFoundError as e:
#     print(f"File not found: {e}")
# finally:
#     if new_data:
#         new_data.close()

def filter_low_scores(threshold, start_date, end_date):
    basket = []
    start_date = datetime.strptime(start_date, "%d-%m-%Y")
    end_date = datetime.strptime(end_date, "%d-%m-%Y")
    try:
        with open("grades.json", "r", encoding="utf-8") as f:
            json_into_dict = json.load(f)
            for line in json_into_dict:
                line_datetime = datetime.strptime(line["date"], "%d-%m-%Y")
                if line["grade"] < threshold and start_date <= line_datetime <= end_date:
                    basket.append(line)
            with open("filtered_low_scores.json", "w", encoding="utf-8") as f2:
                json.dump(basket, f2, indent=4)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(e)
    return basket

# print(filter_low_scores(70, "01-01-2025", "31-03-2025"))

# Task I
"Анализ курсов студентов"
"""Реализуйте программу, которая должна:
1. Прочитать файл student_courses.json, содержащий:
a. Имя,
b. дату рождения (birth_date) в формате дд.мм.гггг,
c. дату поступления (enrollment_date) в том же формате,
d. список курсов.
2. Вычислить:
a. Общее количество студентов.
b. Средний возраст на момент поступления.
c. Количество студентов на каждом курсе.
3. Сохранить отчёт в JSON-файл student_courses_report.json."""

import json
from datetime import datetime

try:
    with open("student_courses.json", "r", encoding="utf-8") as stud_file:
        json_into_dict = json.load(stud_file)
        stud_counter = 0
        age_sum = 0
        subjects = dict()
        for obj in json_into_dict:
            for subj in obj["courses"]:
                subjects[subj] = subjects.get(subj, 0) + 1
            birth_day_df = datetime.strptime(obj["birth_date"], "%d.%m.%Y")
            enrollment_df = datetime.strptime(obj["enrollment_date"], "%d.%m.%Y")
            age_to_enrollment = enrollment_df - birth_day_df
            age_to_enrollment = age_to_enrollment.days // 365
            age_sum += age_to_enrollment
            stud_counter += 1
        res = {}
        avg_age = age_sum // stud_counter
        res["Students overall"] = stud_counter
        res["Average age"] = avg_age
        res["Students per subject"] = subjects
        with open("student_courses_report.json", "w", encoding="utf-8") as result:
            json.dump(res, result, indent=4)
        print(f"Students overall: {stud_counter}")
        print(f"Average age: {avg_age}")
        print(f"Students per subject: {subjects}")
except FileNotFoundError as e:
    print(e)

