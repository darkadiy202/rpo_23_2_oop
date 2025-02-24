import pymysql
import sql_queries


try:
    with (pymysql.connect(host="localhost", port=3306, user="root", password="") as connection):
        print("Connection successful")
        with connection.cursor() as cursor:
            try:
                cursor.execute("""USE students_db""")
            except:
                sql_queries.create_database_and_tables(cursor)
            while True:
                print("1. Отобразить всю информацию.")
                print("2. Отобразить ФИО студентов.")
                print("3. Отобразить все средние оценки у студентов.")
                print("4. Отобразить студентов с оценкой выше, чем указанная.")
                print("5. Отобразить страны студентов без повторов.")
                print("6. Отобразить города студентов без повторов.")
                print("7. Отобразить названия групп без повторов.")
                print("8. Отобразить студентов с самой низкой средней оценкой.")
                print("9. Вставить 5 тестовых студентов.")
                print("0. ВЫХОД.")
                user_choice = input("Веберите действие(номер): ")
                match user_choice:
                    case "0": break
                    case "1": sql_queries.get_full_info(cursor)
                    case "2": sql_queries.get_student_names(cursor)
                    case "3": sql_queries.get_student_average_grades(cursor)
                    case "4": sql_queries.get_students_with_grade_more_than(cursor)
                    case "5": sql_queries.get_student_countries(cursor)
                    case "6": sql_queries.get_student_cities(cursor)
                    case "7": sql_queries.get_student_groups(cursor)
                    case "8": sql_queries.get_worse_students(cursor)
                    case "9": sql_queries.add_test_students(cursor, connection)


except pymysql.err.Error as e:
    print(e)