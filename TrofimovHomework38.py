"1. Безопасная флешка"
"""Создайте класс SecureUSB, представляющий защищённую флешку.
● При создании передаётся секретное содержимое и пароль
● Метод unlock(password) — возвращает True, если пароль верный, и разблокирует флешку
● Метод lock() — блокирует устройство
● Метод read() — возвращает сохранённые данные, если устройство разблокировано, иначе выбрасывает
ошибку PermissionError.
Продумайте, какие поля следует скрыть, а какие оставить доступными.
Пример вывода:
Device is locked.
Access denied.
Access granted.
Data: Secret plans"""

class SecureUSB:
    def __init__(self, secret_intel, init_pswd):
        self.__secret_intel = secret_intel
        self.__init_pswd = init_pswd
        self.__drive_locked = True
    @property
    def drive_locked(self):
        return self.__drive_locked
    def unlock(self, password):
        if password == self.__init_pswd:
            self.__drive_locked = False
            return True
        return False
    def lock(self):
        self.__drive_locked = True
    @property
    def secret_intel(self):
        if self.__drive_locked:
            raise PermissionError("Device is locked!! Unlock it firstly!!")
        return self.__secret_intel

my_flash_usb = SecureUSB("Secret plans", "ps123wd")
print(f"Is Flash Drive locked?: {my_flash_usb.drive_locked}")

try:
    print(my_flash_usb.secret_intel)
    # my_flash_usb.read()
except PermissionError as e:
    print(e)

print("Access granted." if my_flash_usb.unlock("55555pswd") else "Access denied.")
print("Access granted." if my_flash_usb.unlock("ps123wd") else "Access denied.")

"""2. Данные через свойство
Доработайте класс SecureUSB:
● Переделайте метод read() в свойство data, используя @property.
● Теперь доступ к содержимому осуществляется через обращение к usb.data, а не вызов метода.
При попытке чтения в заблокированном состоянии должно по-прежнему выбрасываться
PermissionError.
Пример вывода:
Device is locked. Access denied.
Access granted.
Data: Secret plans"""

print(f"Data: {my_flash_usb.secret_intel}")
print()

"""1. Банковский счёт
Создайте класс BankAccount, описывающий
банковский счёт.
● Объект должен хранить имя владельца и
текущий баланс.
● Реализуйте методы:
○ пополнение счёта
○ снятие средств
○ отображение баланса
● При попытке снять больше, чем есть на счёте,
операция не должна выполняться.
Продумайте, какие поля и методы следует скрыть от
внешнего доступа, а какие оставить открытыми.

Пример вывода:
Current balance: 150
Error: Amount must be positive.
Current balance: 150
Error: Not enough funds.
Current balance: 150"""

class BankAccount:
    def __init__(self, name: str, balance: int | float):
        if balance <= 0:
            raise ValueError("Initial balance must be positive :)")
        self.__name = name
        self.__balance = balance
        self.__history = []
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Error: Amount must be positive.")
        self.__balance += amount
        self.__history.append(f"Deposit: {amount}")
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Error: Amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Error: Not enough funds.")
        self.__balance -= amount
        self.__history.append(f"Withdraw: {amount}")
    @property
    def balance(self):
        return self.__balance
    @property
    def history(self):
        return self.__history[:]

my_account = BankAccount("Anton", 500)
print(f"Current balance: {my_account.balance}")

try:
    my_account.deposit(0)
except ValueError as e:
    print(e)

print(f"Current balance: {my_account.balance}")

try:
    my_account.withdraw(500.1)
except ValueError as e:
    print(e)

print(f"Current balance: {my_account.balance}")
print()

"""2. История операций
Доработайте класс BankAccount.
● Каждая операция пополнения и снятия должна сохраняться в историю.
● История должна быть доступна через property history только для чтения.
● История представляется в виде списка строк ("Deposit: 150", "Withdraw:
100" и т.д.).
Пример вывода:
Current balance: 50
Operation history:
Deposit: 150
Withdraw: 100"""

print(f"Current balance: {my_account.balance}")
my_account.deposit(500)
my_account.deposit(350)
my_account.withdraw(50)
my_account.withdraw(200)
my_account.history.append("Secret injection :D")
# print(my_account.history)
my_history = my_account.history

print(f"Operation history:\n{'\n'.join(my_history)
if my_history else '- No operations exist'}")