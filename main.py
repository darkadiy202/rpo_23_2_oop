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



class Animal:
    animal_counter = 0

    def __init__(self, animal_type, name):
        self.animal_type = animal_type
        self.name = name
        Animal.animal_counter += 1

    def show_info(self):
        print(f"{self.animal_type}; {self.name}")

print(Animal.animal_counter)
barsik = Animal("Cat", "Barsik")
sharik = Animal("Dog", "Sharik")
barsik.show_info()
print(Animal.animal_counter)
print(barsik.animal_counter)
print(sharik.animal_counter)