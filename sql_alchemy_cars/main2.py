from sqlalchemy import create_engine, Column, String, Integer, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from tables import Base
import queries2


if __name__ == "__main__":
    engine = create_engine("sqlite:///cars_database.db")
    Base.metadata.create_all(engine)
    session_factory = sessionmaker(bind=engine)
    session = session_factory()

    while True:
        print("0. Выход.")
        print("1. Добавить много тестовых данных.")
        print("2. Добавить производителя.")
        print("3. Добавить модель.")
        print("4. Добавить пользователя.")
        print("5. Показать все марки машин.")
        print("6. Показать все модели машин.")
        print("7. Показать всех пользователей.")
        print("8. Показать всех пользователей с их машинами.")
        print("9. Показать машины определённой марки.")
        print("10. Показать всех владельцев определённой марки.")
        print("11. Удалить модель машины.")
        print("12. Отредактировать информацию у модели машины.")

        user_choice = input("Ваш выбор(введите номер): ")
        match user_choice:
            case "0": quit()
            case "1": queries2.add_test_many_data(session)
            case "2": queries2.add_brand(session)
            case "3": queries2.add_model(session)
            case "4": queries2.add_user(session)
            case "5": queries2.show_all_brands(session)
            case "6": queries2.show_all_models(session)
            case "7": queries2.show_all_users(session)
            case "8": queries2.show_all_users_with_their_cars(session)
            case "9": queries2.show_all_models_by_brand(session)
            case "10": queries2.show_all_users_by_model(session)
            case "11": queries2.delete_model(session)
            case "12": queries2.update_model(session)
            case _: print("Неверная команда.")