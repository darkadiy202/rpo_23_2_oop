from dataclasses import dataclass


def create_database_and_tables(cursor):
    query = """CREATE DATABASE IF NOT EXISTS students_db"""
    cursor.execute(query)

    query = """USE students_db"""
    cursor.execute(query)

    query = """CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    city VARCHAR(50) NOT NULL,
    country VARCHAR(50) NOT NULL,
    birth_day DATE NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(15) NOT NULL UNIQUE,
    group_name VARCHAR(10),
    avg_grade DECIMAL(3,2),
    worse_discipline VARCHAR(50),
    best_discipline VARCHAR(50)
    )"""
    cursor.execute(query)

    print("База данных и таблицы успешно созданы!")


def add_test_students(cursor, connections):
    query = """INSERT INTO students
                (first_name, last_name, city, country, birth_day, email, phone, group_name, avg_grade, worse_discipline, best_discipline)
                VALUES
                ("Vasya", "Vasin", "Sochi", "Russia", "2000-05-20", "vasya@mail.com", 89006783454, "rpo-23/1", 2.56, "math", "fizra"), 
                ("Petya", "Petin", "Moscow", "Russia", "2008-05-20", "petya@mail.com", 89117683454, "rpo-23/2", 3.56, "fizra", "math"), 
                ("Lionell", "Messi", "Buenos-Aires", "Argentina", "1990-05-20", "messi@mail.com", 89106873445, "rpo-23/2", 4.56, "fizra", "literature"), 
                ("Cristiano", "Ronaldo", "Maderia", "Portugal", "1985-05-20", "cry@mail.com", 89016738444, "rpo-23/2", 4.56, "fizra", "biology"), 
                ("Artyom", "Dzyba", "Moscow", "Russia", "1992-05-20", "dzy@mail.com", 89996783344, "rpo-23/2", 2.56, "operator", "fizra")
    """
    cursor.execute(query)
    connections.commit()
    print("Тестовые студенты успешно добавлены.")



def get_full_info(cursor):
    query = """SELECT * FROM students"""
    cursor.execute(query)
    for row in cursor:
        print(*row, sep="; ")



def get_student_names(cursor):
    query = """SELECT first_name, last_name FROM students"""
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(*row, sep="; ")


def get_student_average_grades(cursor):
    query = """SELECT first_name, last_name, avg_grade FROM students"""
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(*row, sep="; ")


def get_students_with_grade_more_than(cursor):
    grade = int(input("Оценка: "))
    query = f"""SELECT * FROM students WHERE avg_grade > {grade}"""
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(*row, sep="; ")


def get_student_countries(cursor):
    query = """SELECT DISTINCT country FROM students"""
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(*row, sep="; ")


def get_student_cities(cursor):
    query = """SELECT DISTINCT city FROM students"""
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(*row, sep="; ")


def get_student_groups(cursor):
    query = """SELECT DISTINCT group_name FROM students"""
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(*row, sep="; ")


def get_worse_students(cursor):
    query = """SELECT * FROM students
             WHERE avg_grade = (SELECT MIN(avg_grade) FROM students)
    """
    cursor.execute(query)
    data = cursor.fetchall()
    for row in data:
        print(*row, sep="; ")