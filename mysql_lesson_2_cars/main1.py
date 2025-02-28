from re import match


import pymysql
import sql_queries1

try:
    with pymysql.connect(host="localhost", port=3306, user="root", password="") as connection:
        print("Connection successful")
        with connection.cursor() as cursor:
            try:
                cursor.execute("""USE cars""")
            except:
                sql_queries1.create_database_and_tables(cursor)
            while True:
                print("1. Добавить производителя.")
                print("2. Добавить модель машины.")
                print("3. Показать всех производителей.")
                print("4. Показать все модели машин.")
                print("5. Показать все модели конкретного производителя.")
                print("6. Показать все модели машин конкретного года.")
                print("7. Удалить модель машины.")
                print("8. Изменить информацию у модели машины.")
                print("0. Выход.")
                user_choice = input("Ваш выбор(номер): ")
                match user_choice:
                    case "0": break
                    case "1": sql_queries1.add_brand(cursor, connection)
                    case "2": sql_queries1.add_model(cursor, connection)
                    case "3": sql_queries1.show_all_brands(cursor)
                    case "4": sql_queries1.show_all_models(cursor)
                    case "5": sql_queries1.show_models_by_brand(cursor)
                    case "6": sql_queries1.show_models_by_year(cursor)
                    case "7": sql_queries1.delete_model(cursor, connection)
                    case "8": sql_queries1.update_model(cursor, connection)
                    case _: print("Неизвестная команда")


except pymysql.err.Error as e:
    print(e)