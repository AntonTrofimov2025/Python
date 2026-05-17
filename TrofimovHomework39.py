"1. Онлайн-платёжные системы"
"""Создайте абстрактный класс PaymentProcessor.
● В классе должен быть метод pay(amount).
● Реализуйте два класса:
○ PaypalPayment, который печатает 'Paid <amount> via PayPal'.
○ CreditCardPayment, который печатает 'Paid <amount> via Credit Card'.
"""
from abc import ABC, abstractmethod

class InvalidPaymentError(Exception):
    pass

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class PaypalPayment(PaymentProcessor):
    def pay(self, amount):
        if amount <= 0:
            raise InvalidPaymentError('Amount must be positive!!')
        print(f'Paid {amount} via PayPal')

class CreditCardPayment(PaymentProcessor):
    def pay(self, amount):
        if amount <= 0:
            raise InvalidPaymentError('Amount must be positive!!')
        print(f'Paid {amount} via Credit Card')

"""2. Проверка платежей
Доработайте систему:
● Создайте пользовательское исключение InvalidPaymentError.
● В каждом платёжном классе метод pay(amount) должен проверять сумму:
○ Если сумма меньше или равна нулю, выбрасывать InvalidPaymentError.
○ Иначе проводить платёж."""

via_paypal = PaypalPayment()
by_card = CreditCardPayment()

via_paypal.pay(500)
by_card.pay(100)

try:
    via_paypal.pay(0)
except InvalidPaymentError as e:
    print(f"InvalidPaymentError: {e}")
print()

"""1. Фигуры и площади
Создайте абстрактный класс Shape.
● В классе должен быть метод area(), который возвращает площадь фигуры.
● Реализуйте два класса:
○ Circle, который принимает радиус.
○ Rectangle, который принимает ширину и высоту."""
from abc import ABC, abstractmethod
import math

class InvalidSizeError(ValueError):
    pass

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    """
    Represents a circle. Accepts radius.

    Attributes:
        radius (int | float): Radius required for further calculation.
    Methods:
        area(): Returns the calculated area of this circle.
    """
    def __init__(self, radius: int | float):
        if radius <= 0:
            raise InvalidSizeError('Radius must be positive!!')
        self.radius = radius
    def area(self) -> int | float:
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    """
    Represents a rectangle. Accepts width and height.

    Attributes:
        width (int | float): Width required for further calculation.
        height (int | float): Height required for further calculation.
    Methods:
        area(): Returns the calculated area of this rectangle.
    """
    def __init__(self, width: int | float, height: int | float):
        if width <= 0 or height <= 0:
            raise InvalidSizeError('Both width and height must be positive!!')
        self.width = width
        self.height = height
    def area(self) -> int | float:
        return self.width * self.height


"""2. Проверка размеров фигур
Доработайте фигуры:
● Добавьте проверку в конструкторы Circle и Rectangle, чтобы значения были положительными.
● Если передано отрицательное или нулевое значение, выбрасывайте пользовательское исключение
InvalidSizeError."""

try:
    my_circle = Circle(0)
except InvalidSizeError as e:
    print(f"InvalidSizeError: {e}")

try:
    my_rectangle = Rectangle(0, 4)
except InvalidSizeError as e:
    print(f"InvalidSizeError: {e}")

my_circle = Circle(3)
my_rectangle = Rectangle(5, 4)

print(f"{my_circle.area():.2f}")
print(my_rectangle.area())

print(my_circle.__doc__)
print()
print(my_rectangle.__doc__)

