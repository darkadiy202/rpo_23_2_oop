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
import sys
import time
from calendar import firstweekday

import pygame
from pygame.examples.go_over_there import screen


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
# import pickle
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
#         with open("some_square.pkl", "wb") as file:
#             pickle.dump(self, file)
#
#     def load(self):
#         with open("some_square.pkl", "rb") as file:
#             self = pickle.load(file)
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


# import pickle
#
#
# class Book:
#     def __init__(self, title: str, author: str, year: int, genre: str, quantity: int):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.genre = genre
#         self.quantity = quantity
#
#     def __str__(self):
#         return f"{self.title}; {self.author}; {self.year}; {self.genre}; кол-во: {self.quantity}"
#
#
# class Reader:
#     current_reader_id = 1
#
#     def __init__(self, full_name: str):
#         self.full_name = full_name
#         self.book_list = []
#         self.reader_id = Reader.current_reader_id
#         Reader.current_reader_id += 1
#
#     def __str__(self):
#         return f"{self.full_name}. id = {self.reader_id}"
#
#     def add_book(self, book):
#         if isinstance(book, Book) is False:
#             raise TypeError("Can add only class Book objects")
#         self.book_list.append(book)
#
#     def remove_book(self, book):
#         if isinstance(book, Book) is False:
#             raise TypeError("Can add only class Book objects")
#         self.book_list.remove(book)
#
#
# class Library:
#     def __init__(self, name: str, address: str):
#         self.name = name
#         self.address = address
#         self.all_books = []
#         self.all_readers = []
#
#     def __str__(self):
#         return f"{self.name}; {self.address}"
#
#     def show_all_books(self):
#         for book in self.all_books:
#             print(book)
#
#     def show_all_readers(self):
#         for reader in self.all_readers:
#             print(reader)
#
#     def add_book(self, book):
#         if isinstance(book, Book) is False:
#             raise TypeError("Can add only class Book objects")
#         self.all_books.append(book)
#
#     def create_book(self):
#         title = input("Название книги: ")
#         author = input("Автор книги: ")
#         year = int(input("Год издания книги: "))
#         genre = input("Жанр книги: ")
#         quantity = int(input("Общее кол-во книг в библиотеке: "))
#         self.all_books.append(Book(title, author, year, genre, quantity))
#
#     def add_reader(self, reader):
#         if isinstance(reader, Reader) is False:
#             raise TypeError("Can add only class Book objects")
#         self.all_readers.append(reader)
#
#     def create_reader(self):
#         new_name = input("Имя читателя: ")
#         self.all_readers.append(Reader(new_name))
#
#     def book_issue(self, reader, book):
#         if isinstance(reader, Reader) is False or isinstance(book, Book) is False:
#             raise TypeError("Incorrect types of arguments / need Reader and Book")
#         if book.quantity <= 0:
#             print("Данные книги закончились")
#         else:
#             reader.add_book(book)
#             book.quantity -= 1
#
#     def book_return(self, reader, book):
#         if isinstance(reader, Reader) is False or isinstance(book, Book) is False:
#             raise TypeError("Incorrect types of arguments / need Reader and Book")
#         try:
#             reader.remove_book(book)
#             book.quantity += 1
#         except:
#             print("Такой книги у читателя нет!")
#
#     def save_library_data(self):
#         with open("library_data.pkl", "wb") as file:
#             pickle.dump(self, file)
#
#     def load_library_data(self):
#         with open("library_data.pkl", "rb") as file:
#             self = pickle.load(file)
#
#
# war_and_peace = Book("Война и мир", "Толстой Лев Николаевич", 1864, "роман", 5)
# dead_souls = Book("Мёртвые души", "Гоголь Николай Васильевич", 1842, "роман", 2)
#
# vasya = Reader("Вася")
# musk = Reader("Илон Маск")
#
# top_college_library = Library("Библиотека top колледжа", "Куйбышева, д. 11")
#
# top_college_library.add_book(war_and_peace)
# top_college_library.add_book(dead_souls)
#
# top_college_library.show_all_books()


# from abc import ABC, abstractmethod
# from importlib.metadata import pass_none
# from signal import pthread_sigmask
#
#
# class Projectile(ABC):
#     def __init__(self, x, y, angle, speed, damage):
#         self.x = x
#         self.y = y
#         self.angle = angle
#         self.speed = speed
#         self.damage = damage
#
#     @abstractmethod
#     def flying(self):
#         pass
#
#     @abstractmethod
#     def hit(self, other_object):
#         pass
#
# class Arrow(Projectile):
#     def flying(self):
#         print(f"Стрела полетела из координат x:{self.x};y:{self.y} в направлении {self.angle}")
#
#     def hit(self, other_object):
#         print(f"Стрела попала в объект {other_object}")

import pygame
import sys
import random


class Board:
    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.board = [[0 for i in range(width)] for j in range(height)]
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.cell_size = self.height * 10
        self.screen = screen

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(
                    self.screen,
                    self.white,
                    (self.cell_size * x, self.cell_size * y, self.cell_size, self.cell_size),
                    1
                )
        pygame.display.update()


class Minesweeper(Board):
    def __init__(self, width, height, screen, bomb_counter):
        super().__init__(width, height, screen)
        self.bomb_counter = bomb_counter
        self.game_field = [[-1 for i in range(self.width)] for j in range(self.height)]
        self.red = (255, 0, 0)
        self.generate_bomb_positions()
        self.neighbours_cells = (
            (0, -1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1)
        )
        self.text_font = pygame.font.SysFont("Arial", 60)

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                # if self.game_field[y][x] == 10:     # если в таких координатах бомба
                #     # отрисовка бомбы (ПОТОМ УДАЛИТЬ!!!!)
                #     pygame.draw.rect(
                #         self.screen,
                #         self.red,
                #         (self.cell_size * x, self.cell_size * y, self.cell_size, self.cell_size)
                #     )
                if 0 <= self.game_field[y][x] <= 8:
                    bomb_counter_text = self.text_font.render(
                        str(self.game_field[y][x]),
                        1,
                        self.white
                    )
                    self.screen.blit(bomb_counter_text, (x * self.cell_size, y * self.cell_size))
                elif self.game_field[y][x] == 9:
                    # отображение флажка
                    flag_text = self.text_font.render(
                        "?",
                        1,
                        self.white
                    )
                    self.screen.blit(flag_text, (x * self.cell_size, y * self.cell_size))
                # отрисовка сетки
                pygame.draw.rect(
                    self.screen,
                    self.white,
                    (self.cell_size * x, self.cell_size * y, self.cell_size, self.cell_size),
                    1
                )
        pygame.display.update()

    def generate_bomb_positions(self):
        x = 0
        while x < self.bomb_counter:
            bomb_x = random.randint(0, self.width - 1)
            bomb_y = random.randint(0, self.height - 1)
            if self.game_field[bomb_y][bomb_x] == -1:
                self.game_field[bomb_y][bomb_x] = 10        # 10 это бомба
                x += 1

    def click(self, mouse_x, mouse_y, mouse_button):
        x = mouse_x // self.cell_size
        y = mouse_y // self.cell_size
        if mouse_button == 1 and self.game_field[y][x] == -1:
            self.open_cells(x, y)
        elif mouse_button == 1 and self.game_field[y][x] == 10:
            pygame.draw.rect(
                self.screen,
                self.red,
                (self.cell_size * x, self.cell_size * y, self.cell_size, self.cell_size)
            )
            lose_font = pygame.font.SysFont("Arial", 200)
            lose_text = lose_font.render("AHAHA! LOSER!", 1, (0, 255, 255))
            self.screen.blit(lose_text, (100, 400))
            pygame.display.update()
            time.sleep(5)
            pygame.quit()
            sys.exit()
        elif mouse_button == 3:
            if self.game_field[y][x] == -1:
                self.game_field[y][x] = 9
            elif self.game_field[y][x] == 9:
                self.game_field[y][x] = -1
            pygame.display.update()


    def open_cells(self, x, y):
        bomb_counter = 0
        for change_x, change_y in self.neighbours_cells:
            neighbour_x = x + change_x
            neighbour_y = y + change_y
            if 0 <= neighbour_x < self.width and 0 <= neighbour_y < self.height:
                if self.game_field[neighbour_y][neighbour_x] == 10:
                    bomb_counter += 1
        self.game_field[y][x] = bomb_counter

        if self.game_field[y][x] == 0:
            for change_x, change_y in self.neighbours_cells:
                neighbour_x = x + change_x
                neighbour_y = y + change_y
                if 0 <= neighbour_x < self.width and 0 <= neighbour_y < self.height:
                    if self.game_field[neighbour_y][neighbour_x] == -1:
                        self.open_cells(neighbour_x, neighbour_y)


    def check_win(self):
        pass


if __name__ == "__main__":
    width = 15
    height = 10
    pygame.init()
    screen = pygame.display.set_mode((width * 100, height * 100))
    test_board = Minesweeper(width, height, screen, 20)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                test_board.click(event.pos[0], event.pos[1], event.button)
        test_board.render()



























