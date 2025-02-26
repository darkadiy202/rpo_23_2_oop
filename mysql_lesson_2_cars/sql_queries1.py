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
    pass
def delete_model(cursor, connection):
    pass
def update_model(cursor, connection):
    pass
def show_all_brands(cursor):
    pass
def show_all_models(cursor):
    pass
def show_models_by_brand(cursor):
    pass
def show_models_by_year(cursor):
    pass
