from aiogram import Router, F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove
from states import UserStates
import aiohttp
from data import weather_api_token
from all_keyboards import main_keyboard
import time
from datetime import datetime

router = Router()


@router.message(F.text == "Погода", UserStates.user_main_kb)
async def weather(message: types.Message, state: FSMContext):
    await message.answer(
        text="Напишите город, в котором хотите узнать погоду.",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.set_state(UserStates.user_choice_city_weather)


@router.message(F.text, UserStates.user_choice_city_weather)
async def get_weather(message: types.Message, state: FSMContext):
    city = message.text
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_token}&units=metric&lang=ru"
        ) as response:
            if response.status == 200:
                weather_data = await response.json()
                print(weather_data)
                longitude = weather_data["coord"]["lon"]
                latitude = weather_data["coord"]["lat"]
                main_weather = weather_data["weather"][0]["main"]
                description = weather_data["weather"][0]["description"]
                temperature = weather_data["main"]["temp"]
                feels_like = weather_data["main"]["feels_like"]
                pressure = weather_data["main"]["pressure"]
                humidity = weather_data["main"]["humidity"]
                visibility = weather_data["visibility"]
                wind_speed = weather_data["wind"]["speed"]
                wind_degree = weather_data["wind"]["deg"]
                clouds = weather_data["clouds"]["all"]
                timezone = weather_data["timezone"]
                city_time = datetime.fromtimestamp(time.time() - 7200 + timezone)
                sunrise = datetime.fromtimestamp(weather_data["sys"]["sunrise"] + timezone)
                sunset = weather_data["sys"]["sunset"]

                if 45 < wind_degree <= 135:
                    wind_direction = "Восточный"
                elif 135 < wind_degree <= 225:
                    wind_direction = "Южный"
                elif 225 < wind_degree <= 315:
                    wind_direction = "Западный"
                else:
                    wind_direction = "Северный"

                await message.answer(
                    f"Погода: {main_weather}\n"
                    f"Описание: {description}\n"
                    f"Температура: {temperature}°C\n"
                    f"Как ощущается: {feels_like}°C\n"
                    f"Давление: {pressure} гПа\n"
                    f"Влажность: {humidity}\n"
                    f"Скорость ветра: {wind_speed} м/с\n"
                    f"Направление ветра: {wind_direction}\n"
                    f"Облачность: {clouds}%\n"
                    f"Видимость: {visibility}\n"
                    f"Координаты: {longitude};{latitude}\n"
                    f"Местное время: {city_time}\n",
                    reply_markup=main_keyboard()
                )
                await state.set_state(UserStates.user_main_kb)
            else:
                print("Что-то пошло не так😥")







