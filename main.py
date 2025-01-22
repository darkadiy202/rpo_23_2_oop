# class Student:
#     # конструктор(инициализатор)
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hello(self): # метод - объект внутри класса
#         print(f"Hello! My name is {self.name}")
#
#     def get_info(self):
#         return f"{self.name}; {self.age}"
#
# vasya = Student("Vasya", 15)
# petya = Student("Petya", 17)
# print(vasya.name, vasya.age)
# print(petya.name, petya.age)
# vasya.say_hello()
# petya.say_hello()
# print(vasya.get_info())
# print(petya.get_info())
from calendar import firstweekday


#
# class Animal:
#     animal_counter = 0
#
#     def __init__(self, animal_type, name):
#         self.animal_type = animal_type
#         self.name = name
#         Animal.animal_counter += 1
#
#     def show_info(self):
#         print(f"{self.animal_type}; {self.name}")
#
# print(Animal.animal_counter)
# barsik = Animal("Cat", "Barsik")
# sharik = Animal("Dog", "Sharik")
# barsik.show_info()
# print(Animal.animal_counter)
# print(barsik.animal_counter)
# print(sharik.animal_counter)

# class Car:
#     car_counter = 0
#
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price
#         Car.car_counter += 1
#
#     def get_info(self):            #Можно вызвать только через объект
#         return f"{self.brand} {self.model}. Price: {self.price}"
#
#     @classmethod
#     def get_car_counter(cls):         #Можно и через объект, и через класс
#         return cls.car_counter
#
#     @staticmethod
#     def song():                  #Тоже самое, но лучше использовать для каких-нибудь проверок
#         print("BRBRBRBRBRBRRBR")
#
#
#     # @property можно вызвать без скобочек и он связанн с гетерами и сетерами
#
#
# m3 = Car("BMW", "M3", 3_000_000)
# print(m3.get_info())
# print(m3.get_car_counter())
# f40 = Car("Ferrari", "F-40", 30_000_000)
# print(f40.get_car_counter())
#
# print(Car.car_counter)
# print(Car.get_car_counter())
# m3.song()




# class Passport:
#
#     def __init__(self, last_name, first_name, surname, gender, birthday, place_of_birth, serial_number):
#         self.last_name = last_name
#         self.first_name = first_name
#         self.surname = surname
#         self.gender = gender
#         self.birthday = birthday
#         self.place_of_birth = place_of_birth
#         self.serial_number = serial_number
#
#
#     def get_info(self):
#         return (f"Имя: {self.last_name}\nФамилия: {self.first_name}\nОтчество: {self.surname}"
#                 f"\nПол: {self.gender}\nДата рождения: {self.birthday}"
#                 f"\nМесто рождения: {self.place_of_birth}\nСерия и номер: {self.serial_number}")
#
#
# Info = Passport("Никита", "Травинов", "Игоревич", "Муж", 05.06, "Калининград", 2720 )
# print(Info.get_info())



# #ИНКАПСУЛЯЦИЯ
# class Ship:
#     def __init__(self, ship_type, lenght, year):
#         self.ship_type = ship_type   # public
#         self._lenght = lenght         # protected
#         self.__year = year            # private
#
#     def set_year(self, value):
#
#
# titanic = Ship("Пароход", 400, 1909)






# ПОЛИМОРФИЗМ - разное поведение методов в зависимости от того в каком классе мы его вызываем
# class Cat:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     def say(self):
#         print("MEOW!!!")
#
#
# class Dog:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     def say(self):
#         print("BARKBARK!!!")
#
#
# barsik = Cat("Barsik", 15)
# sharik = Dog("Sharik", 10)
# barsik.say()
# sharik.say()

#Наследование

# class Human:
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#
#     def say_hello(self):
#         print(f"Hello! My name is {self.name}!")
#
# class Student(Human):
#     def __init__(self, name, year, group):
#         super().__init__(name, year)
#         self.group = group
#
#
#
# german = Student("German", 2007, "rpo-23/2")
# german.say_hello()


# class Weather:
#
#
#     @staticmethod
#     def celsius_to_fahrenheit(t):
#         return t * 9 / 5 + 32
#
#     @staticmethod
#     def celsius_to_kelvins(t):
#         return t + 273.15
#
#     @staticmethod
#     def fahrenheit_to_celsius(t):
#         return (t - 32) * 5/9
#
#     @staticmethod
#     def fahrenheit_to_kelvins(t):
#         return (t - 32) * 5/9 + 273.15
#
#     @staticmethod
#     def kelvins_to_celsius(t):
#         return t - 273.15
#
#     @staticmethod
#     def kelvins_to_fahrenheit(t):
#         return (t - 273.15) * 9/5 + 32


# import math
#
# class Fraction:
#     def __init__(self, numerator, denominator):
#         self.a = numerator
#         self.b = denominator
#         self.reduction()
#
#     def __str__(self):
#         return f"{self.a}/{self.b}"
#
#     def summ(self, other):
#         return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)
#
#     def subtraction(self, other):
#         return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)
#
#     def multiplication(self, other):
#         return Fraction(self.a * other.a, self.b * other.b)
#
#     def division(self, other):
#         return Fraction(self.a * other.b, self.b * other.a)
#
#     def __add__(self, other):
#         return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)
#
#     def __sub__(self, other):
#         return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)
#
#     def __mul__(self, other):
#         return Fraction(self.a * other.a, self.b * other.b)
#
#     def __truediv__(self, other):
#         return Fraction(self.a * other.b, self.b * other.a)
#
#     def __iadd__(self, other):
#         self.a = self.a * other.b + self.b * other.a
#         self.b = self.b * other.b
#         return self
#
#     def __isub__(self, other):
#         self.a = self.a * other.b - self.b * other.a
#         self.b = self.b * other.b
#         return self
#
#     def __imul__(self, other):
#         self.a = self.a * other.a
#         self.b = self.b * other.b
#         return self
#
#     def __itruediv__(self, other):
#         self.a, self.b = self.a * other.b, self.b * other.a
#         return self
#
#
#     def __gt__(self, other):
#         return self.a * other.b > self.b * other.a
#
#
#     def __lt__(self, other):
#         return self.a * other.b < self.b * other.a
#
#     def __eq__(self, other):
#         return self.a * other.b == self.b * other.a
#
#     def __ne__(self, other):
#         return self.a * other.b != self.b * other.a
#
#     def __ge__(self, other):
#         return self.a * other.b >= self.b * other.a
#
#     def __le__(self, other):
#         return self.a * other.b <= self.b * other.a
#
#     def reduction(self):
#         common_divider = math.gcd(self.a, self.b)
#         self.a = self.a // common_divider
#         self.b = self.b // common_divider
#
#
#
#
#
#
#
# first = Fraction(2, 5)
# print(first)
# second = Fraction(2, 3)
# print(first.summ(second))
# print(first.division(second))
# print(first.multiplication(second))
# print(first + second)
# print(first - second)
# print(first / second)
# first += second
# print(first)
# print(first > second)
#
# print(math.gcd(8, 10))
# print(math.gcd(100, 200))
#
# print(Fraction(50, 100) * (Fraction(2, 2)))

# import math
#
# class MyMath:
#     @staticmethod
#     def max_argument(a, b, c, d):
#         return max(a, b, c, d)
#
#     @staticmethod
#     def min_argument(a, b, c, d):
#         return min(a, b, c, d)
#
#     @staticmethod
#     def avg_of_four(a, b, c, d):
#         return (a + b + c + d) / 4
#
#     @staticmethod
#     def factorial(n):
#         return math.factorial(n)
#
#
# print(MyMath.factorial(5))



# from abc import ABC, abstractmethod
#
#
# class Figure2D(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#     @abstractmethod
#     def perimeter(self):
#         pass
#
#
# class Square(Figure2D):
#     def __init__(self, size):
#         self.size = size
#
#     def area(self):
#         return self.size ** 2
#
#     def perimeter(self):
#         return self.size * 4
#
#
# class Rectangle(Figure2D):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def area(self):
#         return self.width * self.height
#
#     def perimeter(self):
#         return (self.width + self.height) * 2


# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hi(self):
#         print(f"Hi! My name is {self.name}")
#
#
# class Builder(Human):
#     def __init__(self, name, age, specialization):
#         super().__init__(name, age)
#         self.specialization = specialization
#
#     def build_roof(self):
#         print(f"{self.name} building a roof!")
#
#
# class Sailor(Human):
#     def __init__(self, name, age, ship):
#         super().__init__(name, age)
#         self.ship = ship
#
#     def drink_rome(self):
#         print(f"{self.name} drinking holy water!")
#
#
# class Pilot(Human):
#     def __init__(self, name, age, airplane):
#         super().__init__(name, age)
#         self.airplane = airplane
#
#     def flying(self):
#         print(f"{self.name} flying on {self.airplane}!")


# class Animal:
#     def __init__(self, name, age, weight, height):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.height = height
#
#     def say(self):
#         pass
#
#     def eat(self):
#         pass
#
#
# class Tiger(Animal):
#     def say(self):
#         print("МЯУ")
#
#     def eat(self):
#         print("ТИГР КУШОЕТ")
#
# class Crocodile(Animal):
#     def say(self):
#         print("Иди сюда чебурашка")
#
#     def eat(self):
#         print("КРОКОДАЙЛ КУШОЕТ")
#
# class Kangaroo(Animal):
#     def say(self):
#         print("ГАВ ГАВ")
#
#     def eat(self):
#         print("КЕНГУРУ КУШОЕТ")
#
#
# sherhan = Tiger("Шер хан", 20, 450, 150)
# Tiger.eat(sherhan)
# Tiger.say(sherhan)

# class Money:
#     def __init__(self, valuta: str, left: int, right: int):
#         self.valuta = valuta
#         self.a = left
#         self.b = right
#
#     def __str__(self):
#         if self.b < 10:
#             return f"{self.a}.0{self.b} {self.valuta}"
#         return f"{self.a}.{self.b} {self.valuta}"
#
#     def set_left(self, value):
#         self.a = value
#
#     def set_right(self, value):
#         self.b = value
#
#     def __add__(self, other):
#         if self.valuta != other.valuta:
#             raise ValueError("Dont summ different valuta")
#         else:
#             new_b = self.b + other.b
#             if new_b > 99:
#                 return Money(self.valuta, self.a + other.a + 1, new_b - 100)
#             return Money(self.valuta, self.a + other.a, new_b)
#
#     def __sub__(self, other):
#         if self.valuta != other.valuta:
#             raise ValueError("Dont summ different valuta")
#         else:
#             new_b = self.b - other.b
#             if new_b < 0:
#                 return Money(self.valuta, self.a - other.a - 1, new_b + 100)
#             return Money(self.valuta, self.a - other.a, new_b)
#
#
# vasyas_pocket = Money("USD", 35, 20)
# print(vasyas_pocket)
# petyas_pocket = Money("USD", 100, 80)
# print(vasyas_pocket + petyas_pocket)
# print(vasyas_pocket - petyas_pocket)


# import pygame
#
#
# class Shape:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def show(self):
#         pass
#
#     def save(self):
#         pass
#
#     def load(self):
#         pass
#
# class Square(Shape):
#     def __init__(self, x: int, y: int, size: int, color: tuple[int, int, int]):
#         super().__init__(x, y)
#         self.size = size
#         self.color = color
#
#     def show(self):
#         pygame.draw.rect(
#             screen,
#             self.color,
#             (self.x, self.y, self.size, self.size)
#         )
#         pygame.display.update()
#
#     def save(self):
#         pass
#
#     def load(self):
#         pass
#
#
# class Rectangle(Shape):
#     def __init__(self, x: int, y: int, width: int, height: int, color: tuple[int, int, int]):
#         super().__init__(x, y)
#         self.width = width
#         self.height = height
#         self.color = color
#
#     def show(self):
#         pygame.draw.rect(
#             screen,
#             self.color,
#             (self.x, self.y, self.width, self.height)
#         )
#         pygame.display.update()
#
#     def save(self):
#         pass
#
#     def load(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self, x: int, y: int, radius: int, color: tuple[int, int, int]):
#         super().__init__(x, y)
#         self.radius = radius
#         self.color = color
#
#     def show(self):
#         pygame.draw.circle(
#             screen,
#             self.color,
#             (self.x, self.y),
#             self.radius
#         )
#         pygame.display.update()
#
#     def save(self):
#         pass
#
#     def load(self):
#         pass
#
#
# pygame.init()
# screen = pygame.display.set_mode((1000, 1000))
#
#
# sponge_bob = Square(50, 50, 100,(255, 255, 0))
#
# sponge_bob_father = Square(350, 350, 200, (255, 200, 0))
#
# brick = Rectangle(500, 500, 200, 100, (255, 0, 0))
#
# kolobok = Circle(600, 800, 100, (200, 200, 0))
# kolobok_change_y = 5
# while True:
#     pygame.time.Clock().tick(10)
#     screen.fill((0, 0, 0))
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#
#     kolobok.y += kolobok_change_y
#     if kolobok.y > 800 or kolobok.y < 0:
#         kolobok_change_y *= -1
#
#     kolobok.show()
#     brick.show()
#     sponge_bob_father.show()
#     sponge_bob.show()
