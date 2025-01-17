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


import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.a = numerator
        self.b = denominator
        self.reduction()

    def __str__(self):
        return f"{self.a}/{self.b}"

    def summ(self, other):
        return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)

    def subtraction(self, other):
        return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)

    def multiplication(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def division(self, other):
        return Fraction(self.a * other.b, self.b * other.a)

    def __add__(self, other):
        return Fraction(self.a * other.b + self.b * other.a, self.b * other.b)

    def __sub__(self, other):
        return Fraction(self.a * other.b - self.b * other.a, self.b * other.b)

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        return Fraction(self.a * other.b, self.b * other.a)

    def __iadd__(self, other):
        self.a = self.a * other.b + self.b * other.a
        self.b = self.b * other.b
        return self

    def __isub__(self, other):
        self.a = self.a * other.b - self.b * other.a
        self.b = self.b * other.b
        return self

    def __imul__(self, other):
        self.a = self.a * other.a
        self.b = self.b * other.b
        return self

    def __itruediv__(self, other):
        self.a, self.b = self.a * other.b, self.b * other.a
        return self


    def __gt__(self, other):
        return self.a * other.b > self.b * other.a


    def __lt__(self, other):
        return self.a * other.b < self.b * other.a

    def __eq__(self, other):
        return self.a * other.b == self.b * other.a

    def __ne__(self, other):
        return self.a * other.b != self.b * other.a

    def __ge__(self, other):
        return self.a * other.b >= self.b * other.a

    def __le__(self, other):
        return self.a * other.b <= self.b * other.a

    def reduction(self):
        common_divider = math.gcd(self.a, self.b)
        self.a = self.a // common_divider
        self.b = self.b // common_divider







first = Fraction(2, 5)
print(first)
second = Fraction(2, 3)
print(first.summ(second))
print(first.division(second))
print(first.multiplication(second))
print(first + second)
print(first - second)
print(first / second)
first += second
print(first)
print(first > second)

print(math.gcd(8, 10))
print(math.gcd(100, 200))

print(Fraction(50, 100) * (Fraction(2, 2)))
