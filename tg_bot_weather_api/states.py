from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    user_main_kb = State()
    user_weather = State()
    user_choice_city_weather = State()
    user_choice_country = State()
    country = State()
