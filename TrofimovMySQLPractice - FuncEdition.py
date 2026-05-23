import os

import pymysql
from dotenv import load_dotenv

show_me_departments = """
SELECT DENSE_RANK() OVER (ORDER BY department_id) as num, department_name
from departments
"""

choose_your_dep = """
SELECT d.department_name FROM departments d
  JOIN
    (select department_id, dense_rank() over (order by department_id) as dep_rank from departments)
    as dr ON d.department_id = dr.department_id
  WHERE dr.dep_rank = %s"""

first_emp_name_and_dep = """
SELECT DISTINCT e.first_name, rk.dep_rank, rk.department_name
FROM employees e
       RIGHT JOIN (SELECT dense_rank() over (order by department_id) as dep_rank, department_id, department_name
                   from departments) rk ON e.department_id = rk.department_id
where rk.dep_rank = %s"""

def main():

    load_dotenv('.env')

    with pymysql.connect(
        host=os.environ.get('DB_HOST', 'localhost'),
        user=os.environ.get('DB_USER', 'user'),
        password=os.environ.get('DB_PASSWORD', 'password'),
        database=os.environ.get('DB_DATABASE', 'test'),
    ) as conn:  # автоматически закроет connection
        with conn.cursor() as cursor:  # автоматически закроет cursor
            def show_all_deps():
                while True:
                    try:
                        show_dep = input("Show departments? (y/n): ")
                        if show_dep.lower().strip() == "y":
                            cursor.execute(show_me_departments)
                            print("List of departments: ",
                                  *(f"{num}. {department_name}" for num, department_name in cursor), sep="\n")
                            break
                        elif show_dep.lower().strip() == "n":
                            break
                        else:
                            continue
                    except ValueError:
                        print("Use 'y' or 'n' only!!")

            def department_selection():
                while True:
                    try:
                        your_department = int(input('Enter department number: '))
                    except ValueError:
                        print("Invalid department number. Please try again.")
                    else:
                        cursor.execute(choose_your_dep, (your_department,))
                        department_exists = cursor.fetchone()
                        if department_exists:
                            break
                        print("Invalid department number. Please try again.")
                cursor.execute(first_emp_name_and_dep, (your_department,))
                first_emp = cursor.fetchone()
                return first_emp, your_department

            def is_filter():
                while True:
                    filtering = input("Would you like to filter employees by salary? (y/n): ").lower().strip()
                    if filtering in ("y", "n"):
                        break
                    print("Use 'y' or 'n' only!!")

                return filtering == "y"

            def select_comparison():
                while True:
                    condition = input("Enter condition (>, <, =, >=, <=): ")
                    if condition in (">", "<", "=", ">=", "<="):
                        # your_operator = ">" if condition == ">" else ("<" if condition == "<" else (
                        #     "=" if condition == "=" else (">=" if condition == ">=" else "<=")))
                        return condition
                    print("Use indicated operators only!!")

            def enter_salary():
                while True:
                    try:
                        salary = float(input("Enter salary: "))
                        return salary
                    except ValueError:
                        print("Please use numbers only.")
            # cursor.execute('SHOW Tables')
            # for table in cursor:
            #     print(table)
            # cursor.execute('DESCRIBE employees')
            # for type_ in cursor:
            #     print(type_)
            # print()
            show_all_deps()
            first_emp, your_department = department_selection()
            first_emp_name = first_emp[0]
            first_emp_dep = first_emp[2]
            salary = 0
            your_operator = ">="
            if first_emp_name:
                if is_filter():
                    your_operator = select_comparison()
                    salary = enter_salary()
            else:
                salary = None
                your_operator = "is"
            cursor.execute(f"""SELECT ROW_NUMBER() OVER (order by e.salary DESC) AS row_num, e.first_name, e.last_name,
                j.job_title, e.salary, d.department_name, d.department_id
                FROM
                    departments d
                        LEFT JOIN
                    employees e ON d.department_id = e.department_id
                        LEFT JOIN
                    jobs j ON e.job_id = j.job_id
                        JOIN
                    (select department_id, dense_rank() over (order by department_id) as dep_rank from departments)
                    as dr ON d.department_id = dr.department_id
                WHERE dr.dep_rank = %s and e.salary {your_operator} %s
                ORDER BY e.salary DESC""", (your_department, salary) )
            all_data = cursor.fetchall()
            first_employee_name = None
            if all_data:
                first_employee_name = all_data[0][1]
            if first_employee_name:
                print(f"Your choice: {first_emp_dep}")
                for _id, f_name, l_name, j_title, salary, _, _ in all_data:
                        print(f'{_id}. {f_name} {l_name} — {j_title} — {salary}')

            else:
                print(f"Your choice: {first_emp_dep}")
                print(f"No employees found in {first_emp_dep} department.")

if __name__ == "__main__":
    main()

"""1. Список сотрудников по убыванию зарплаты
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