"1. Класс Employee"
"""Создайте класс Employee, представляющий сотрудника.
● У каждого объекта должно быть поле name.
● Метод work() выводит строку: <имя> is working....
● Проверьте работу класса, создав сотрудника и вызвав метод work().
Пример вывода:
Alice is working..."""

class Employee:
    def __init__(self, name):
        self.name = name
    def work(self):
        print(f"{self.name} is working...")

my_employee = Employee("Fedor")
my_employee.work()
print()

"2. Класс Developer"
"""Создайте класс Developer, который расширяет Employee.
● Добавьте дополнительное поле language.
● Переопределите метод work(), чтобы он включал сообщение из родительского метода и добавлял
строку:
<имя> writes <язык> code.
● Проверьте работу, создав объект Developer и вызвав метод work().
Пример вывода:
Bob is working...
Bob writes Python code."""

class Developer(Employee):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language
    def work(self):
        super().work()
        print(f"{self.name} writes {self.language} code.")

my_dev = Developer("Bob", "Python")
my_dev.work()
print()

"1. Класс Person"
"""Создайте класс Person, представляющий человека.
● Каждый человек должен иметь имя.
● Добавьте метод introduce(), который выводит приветствие с именем.
Пример вывода:
Hello, my name is Alice."""

class Person:
    def __init__(self, name: str):
        self.name = name
    def introduce(self):
        print(f"Hello, my name is {self.name}.")

my_person = Person("Alice")
my_person.introduce()
print()

"2. Класс Student"
"""На основе класса Person создайте класс Student.
● Студент должен иметь имя и номер курса.
● Метод introduce() должен сначала выводить базовое приветствие, а затем
строку: I'm on course <номер_курса>.
Пример вывода:
Hello, my name is Alice.
I'm on course 2."""

class Student(Person):
    def __init__(self, name: str, course: int):
        super().__init__(name)
        self.course = course
    def introduce(self):
        super().introduce()
        print(f"I'm on course {self.course}.")

my_student = Student("Alice", 2)
my_student.introduce()
print()

"3. Класс Teacher и список людей"
"""На основе класса Person создайте класс Teacher.
● У преподавателя есть имя и предмет.
● Метод introduce() должен выводить имя и предмет.
● Метод introduce() должен выводить строку: Hello, I am professor <имя>.
My subject is <предмет>.
● Создайте список, в котором будут Student и Teacher, и вызовите у всех метод
introduce().
Пример вывода:
Hello, my name is Alice.
I'm on course 2.
Hello, I am professor Bob.
My subject is Mathematics"""

class Teacher(Person):
    def __init__(self, name: str, subject: str):
        super().__init__(name)
        self.subject = subject
    def introduce(self):
        print(f"Hello, I am professor {self.name}.\nMy subject is {self.subject}.")

my_teacher = Teacher("Bob", "Mathematics")
people = [my_student, my_teacher]

for person in people:
    person.introduce()