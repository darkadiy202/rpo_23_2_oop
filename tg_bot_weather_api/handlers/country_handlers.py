from aiogram import Router, F, types
import requests
from aiogram.fsm.context import FSMContext
import random

from all_keyboards import main_keyboard
from states import UserStates

router = Router()

all_countries_data = requests.get("https://restcountries.com/v3.1/all").json()


@router.message(F.text == "Страны", UserStates.user_main_kb)
async def coutries(message: types.Message, state: FSMContext):
    random_country = random.choice(all_countries_data)
    print(random_country)
    country_name = random_country["translations"]["rus"]["common"]
    country_official_name = random_country["translations"]["rus"]["official"]
    country_area = random_country["area"]
    country_population = random_country["population"]
    country_capital = random_country["capital"][0]

    await message.answer(
        f"Столица: {country_capital}\n"
        f"Население страны: {country_population}\n"
        f"Площадь страны: {country_area}\n"
        f"Что это за страна?"
    )
    await state.set_state(UserStates.user_choice_country)
    await state.update_data(country=country_name)



@router.message(F.text, UserStates.user_choice_country)
async def check_country_answer(message: types.Message, state: FSMContext):
    user_answer = message.text
    data = await state.get_data()
    country = data["country"]
    # print(user_answer, country)

    result = "Правильно!" if user_answer.lower() == country.lower() else f"Непраивльно\n Правильный ответ: {country}"

    await message.reply(
        result,
        reply_markup=main_keyboard()
    )
    await state.set_state(UserStates.user_main_kb)