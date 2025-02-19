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