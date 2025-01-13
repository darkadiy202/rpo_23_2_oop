class Student:
    # конструктор(инициализатор)
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self): # метод объектов в этом классе
        return f"Hello! My name is {self.name}"

    def get_info(self):
        return f"{self.name}; {}"

vasya = Student("Vasya", 15)
petya = Student("Petya", 17)
print(vasya.name, vasya.age)
print(petya.name, petya.age)
vasya.say_hello()
petya.say_hello()
print(vasya.get_info())
print(petya.get_info())
