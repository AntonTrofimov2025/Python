import pymysql
import os
from dotenv import load_dotenv

load_dotenv('.env')

with pymysql.connect(
    host=os.environ.get('DB_HOST', 'localhost'),
    user=os.environ.get('DB_USER', 'user'),
    password=os.environ.get('DB_PASSWORD', 'password'),
    database=os.environ.get('DB_DATABASE', 'test'),
) as conn:  # автоматически закроет connection
    with conn.cursor() as cursor:  # автоматически закроет cursor
        # cursor.execute('SHOW Tables')
        # for table in cursor:
        #     print(table)
        # cursor.execute('DESCRIBE employees')
        # for type_ in cursor:
        #     print(type_)
        # print()
        while True:
            try:
                your_department = int(input('Enter department number: '))
            except ValueError:
                print("Invalid department number. Please try again.")
            else:
                cursor.execute("""SELECT d.department_name FROM hr.departments d
                                  JOIN
                                    (select department_id, dense_rank() over (order by department_id) as dep_rank from hr.departments)
                                    as dr ON d.department_id = dr.department_id
                                  WHERE dr.dep_rank = %s""", (your_department, ))
                department_exists = cursor.fetchone()
                if department_exists:
                    break
                else:
                    print("Invalid department number. Please try again.")
        # print(f"Your choice: {cursor.fetchone()[0]}")
        cursor.execute("""SELECT ROW_NUMBER() OVER (order by e.salary DESC) AS row_num, e.first_name, e.last_name,
                        j.job_title, e.salary, d.department_name, d.department_id
                        FROM
                            hr.departments d
                                LEFT JOIN
                            hr.employees e ON d.department_id = e.department_id
                                LEFT JOIN
                            hr.jobs j ON e.job_id = j.job_id
                                JOIN
                            (select department_id, dense_rank() over (order by department_id) as dep_rank from hr.departments)
                            as dr ON d.department_id = dr.department_id
                        WHERE dr.dep_rank = %s
                        ORDER BY e.salary DESC""", (your_department, ) )
        all_data = cursor.fetchall()
        if all_data:
            print(f"Your choice: {all_data[0][5]}")
            if all_data[0][1] is None:
                print(f"No employees found in {all_data[0][5]} department.")
            else:
                condition = None
                salary = None
                filtering = input("Would you like to filter employees by salary? (y/n): ")
                if filtering.lower().strip() == "y":
                    condition = input("Enter condition (>, <, =, >=, <=): ")
                    if condition not in (">", "<", "=", ">=", "<="):
                        condition = None
                    try:
                        salary = int(input("Enter salary: "))
                    except Exception:
                        salary = None
                if condition or salary:
                    try:
                        for employee in all_data:
                            if condition == ">" and employee[4] > salary:
                                print(f'{employee[0]}. {employee[1]} {employee[2]} — {employee[3]} — {employee[4]}')
                            elif condition == "<" and employee[4] < salary:
                                print(f'{employee[0]}. {employee[1]} {employee[2]} — {employee[3]} — {employee[4]}')
                            elif condition == ">=" and employee[4] >= salary:
                                print(f'{employee[0]}. {employee[1]} {employee[2]} — {employee[3]} — {employee[4]}')
                            elif condition == "<=" and employee[4] <= salary:
                                print(f'{employee[0]}. {employee[1]} {employee[2]} — {employee[3]} — {employee[4]}')
                            elif condition == "=" and employee[4] == salary:
                                print(f'{employee[0]}. {employee[1]} {employee[2]} — {employee[3]} — {employee[4]}')
                    except TypeError:
                        for employee in all_data:
                            print(f'{employee[0]}. {employee[1]} {employee[2]} — {employee[3]} — {employee[4]}')
                else:
                    for employee in all_data:
                        print(f'{employee[0]}. {employee[1]} {employee[2]} — {employee[3]} — {employee[4]}')
        # else:
        #     print("Department empty or not found or doesn't exist.")

"""1. Список сотрудников по убыванию
зарплаты
Добавьте к программе сортировку сотрудников выбранного департамента по убыванию зарплаты. Выведите имя,
фамилию, должность и зарплату каждого сотрудника, начиная с самого высокооплачиваемого. Также добавьте
нумерацию (не id).
Пример вывода:
Enter department: Marketing
1. Michael Hartstein — Marketing Manager — 13000.00
2. Pat Fay — Marketing Representative — 6000.00"""

"""2. Выбор департамента по номеру
Модифицируйте предыдущую программу так, чтобы пользователь выбирал департамент по номеру из списка, а
не вручную вводил его название. После выбора выведите название департамента и продолжите выполнение.
Пример вывода:
Enter department number: 2
You choose: Marketing
1. Michael Hartstein — Marketing Manager — 13000.00
2. Pat Fay — Marketing Representative — 6000.00"""

"""3. Пустой департамент
Добавьте в программу проверку: если в выбранном департаменте нет сотрудников, вместо списка
сотрудников выведите сообщение:
No employees found in this department.
Пример вывода:
Enter department number: 27
You selected: Payroll
No employees found in Payroll department."""

"""4. Фильтрация сотрудников по
зарплате
Если в выбранном департаменте есть сотрудники — добавьте возможность отфильтровать
их по зарплате.
Спросите пользователя:
Would you like to filter employees by salary? (y/n)
Если ответ — y, попросите ввести знак сравнения и значение:
Enter condition (>, <, =, >=, <=): >
Enter salary: 13000
Затем выведите только тех сотрудников, которые соответствуют критерию. Если ответ —
n, просто выведите всех сотрудников."""

"""5. Повторный ввод при ошибке
Модифицируйте программу так, чтобы при вводе некорректного номера департамента
пользователю предлагалось ввести его снова. Программа не должна завершаться, пока не
будет введён корректный номер.
Пример вывода:
Enter department number: 999
Invalid department number. Please try again.
Enter department number: num1
Invalid input. Please enter a number.
Enter department number: 2
You selected: Marketing"""