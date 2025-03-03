from dataclasses import dataclass


def create_database_and_tables(cursor):
    cursor.execute("""CREATE DATABASE IF NOT EXISTS cars""")
    cursor.execute("""USE cars""")

    query = """CREATE TABLE IF NOT EXISTS brands (
                id INT AUTO_INCREMENT PRIMARY KEY,
                brand_name VARCHAR(50) NOT NULL UNIQUE,
                country VARCHAR(50) NOT NULL
    )"""
    cursor.execute(query)

    query = """CREATE TABLE IF NOT EXISTS models (
                id INT AUTO_INCREMENT PRIMARY KEY,
                model_name VARCHAR(50) NOT NULL,
                year INT NOT NULL,
                price INT NOT NULL,
                max_speed INT NOT NULL,
                brand_id INT NOT NULL,
                FOREIGN KEY (brand_id) REFERENCES brands(id)
    )"""
    cursor.execute(query)

    print("База данных и таблицы успешно созданы.")

def add_brand(cursor, connection):
    name = input("Производитель: ").title()
    country = input("Страна: ").title()
    query = """INSERT INTO brands (brand_name, country) VALUE (%s, %s)"""
    cursor.execute(query, (name, country))
    connection.commit()
    print("Производитель успешно добавлен.")


def add_model(cursor, connection):
    show_all_brands(cursor)
    brand_id = int(input("Выберите id производителя: "))
    model_name = input("Название модели: ")
    year = int(input("Годы выпуска: "))
    max_speed = int(input("Максимальная скорость: "))
    price = int(input("Цена: "))
    query = """INSERT INTO models
                (model_name, year, price, max_speed, brand_id)
                VALUES
                (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (model_name, year, price, max_speed, brand_id))
    connection.commit()
    print(f"Модель {model_name} успешно добавлена.")


def delete_model(cursor, connection):
    show_all_models(cursor)
    model_id = int(input("Выберите id модели, которую надо удалить: "))
    query = """DELETE FROM models
                WHERE id = %s
    """
    cursor.execute(query, model_id)
    connection.commit()
    print("Машина успешно удалена.")



def update_model(cursor, connection):
    show_all_models(cursor)
    model_id = int(input("Выберите id модели, которую надо отредактировать: "))
    model_name = input("Название модели: ")
    year = int(input("Годы выпуска: "))
    max_speed = int(input("Максимальная скорость: "))
    price = int(input("Цена: "))
    query = """UPDATE models
                SET model_name = %s, year = %s, max_speed = %s, price = %s
                WHERE id = %s
    """
    cursor.execute(query, (model_name, year, max_speed, price, model_id))
    connection.commit()
    print("Информация успешно обновлена.")


def show_all_brands(cursor):
    query = """SELECT id, brand_name, country FROM brands"""
    cursor.execute(query)
    data = cursor.fetchall()
    print("Все производители: ")
    for row in data:
        print(*row, sep="; ")
    print("\n\n")


def show_all_models(cursor):
    query = """SELECT m.id, b.brand_name, m.model_name, m.year, b.country, m.max_speed, m.price FROM models m
                JOIN brands b
                WHERE m.brand_id = b.id
                ORDER BY (b.brand_name)
    """
    cursor.execute(query)
    data = cursor.fetchall()
    print("Все модели: ")
    for row in data:
        print(*row, sep="; ")
    print("\n\n")


def show_models_by_brand(cursor):
    show_all_brands(cursor)
    brand_id = int(input("Выберите id производителя: "))
    query = """SELECT model_name, year, max_speed, price FROM models
                WHERE brand_id = %s
                ORDER BY (model_name)
    """
    cursor.execute(query, brand_id)
    data = cursor.fetchall()
    print("Все модели данного производителя: ")
    for row in data:
        print(*row, sep="; ")
    print("\n\n")


def show_models_by_year(cursor):
    show_all_models(cursor)
    year = int(input("Выберите год производителя: "))
    query = """SELECT model_name, year, max_speed, price FROM models
                WHERE year = %s
                ORDER BY (model_name)
    """
    cursor.execute(query, year)
    data = cursor.fetchall()
    print("Все модели данного года: ")
    for row in data:
        print(*row, sep="; ")
    print("\n\n")


def add_users_table(cursor):
    query = """CREATE TABLE IF NOT EXISTS users (
               id INT AUTO_INCREMENT PRIMARY KEY,
               first_name VARCHAR(50) NOT NULL,
               last_name VARCHAR(50) NOT NULL, 
               phone VARCHAR(15) NOT NULL UNIQUE
    )"""
    cursor.execute(query)

    query = """CREATE TABLE IF NOT EXISTS users_and_cars (
               user_id INT,
               car_id INT,
               PRIMARY KEY (user_id, car_id),
               FOREIGN KEY (user_id) REFERENCES users(id),
               FOREIGN KEY (car_id) REFERENCES models(id)
    )"""
    cursor.execute(query)

    print("Таблица про пользователей успешно создана.")


def add_user(cursor, connection):
    first_name = input("Имя: ")
    last_name = input("Фамилия: ")
    phone = input("Телефон: ")
    query = """INSERT INTO users
                (first_name, last_name, phone)
                VALUES
                (%s, %s, %s)
    """
    cursor.execute(query, (first_name, last_name, phone))
    connection.commit()
    print(f"Пользователь {first_name} {last_name} успешно добавлен")

def show_users_list(cursor):
    pass

def add_car_to_user(cursor, connection):
    pass

def show_cars_by_user(cursor):
    pass

def show_users_by_car(cursor):
    pass
