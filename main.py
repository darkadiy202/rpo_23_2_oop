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




