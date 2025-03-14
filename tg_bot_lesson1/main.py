import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command, CommandObject
from aiogram import F
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import KeyboardButton, KeyboardBuilder, InlineKeyboardButton, InlineKeyboardBuilder, ReplyKeyboardMarkup
import logging


logging.basicConfig(level=logging.INFO)

bot = Bot(token="7854780999:AAFfx3LPcquop89vjIUc4QLIyJhl_vnFgU8")
dp = Dispatcher()


@dp.message(Command("start"))       # /start
async def start(message: types.Message):
    await message.answer("HI!!!")


@dp.message(Command("дурак"))       # /дурак
async def durak(message: types.Message):
    await message.reply("Сам такой!!!")


@dp.message(Command("dice"))       # /dice
async def dice(message: types.Message):
    await message.answer_dice(emoji="🎲")


@dp.message(Command("rickroll"))       # /rickroll
async def rickroll(message: types.Message):
    await message.answer_sticker(sticker="https://spotify-rickroll.vercel.app/static/rick.webp")    # ТОЛЬКО WEBP

@dp.message(Command("htmltest"))       # /htmltest
async def htmltest(message: types.Message):
    await message.answer(
        "<i>Ты</i> <b>Гений</b>",
        parse_mode=ParseMode.HTML
    )

@dp.message(Command("myprefix", prefix="."))
async def myprefix(message: types.Message):
    await message.answer("Sigma Boy!")

@dp.message(Command("choice"))
async def choice(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Бобёр")],
        [types.KeyboardButton(text="Сигма бой")]
    ]
    keyboard_markup = ReplyKeyboardMarkup(
        keyboard=kb,
        input_field_placeholder="Что выберешь?",
        resize_keyboard=True
    )
    await message.answer("Отвечай!!!!", reply_markup=keyboard_markup)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())