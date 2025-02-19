import pymysql
import sql_queries

try:
    with pymysql.connect(host="localhost", port=3306, user="root", password="") as connection:
        print("Connection successful")
        with connection.cursor() as cursor:
            try:
                cursor.execute("""USE students_db""")
            except:
                sql_queries.create_database_and_tables(cursor)
except pymysql.err.Error as e:
    print(e)