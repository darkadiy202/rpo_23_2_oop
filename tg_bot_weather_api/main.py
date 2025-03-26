import asyncio
from aiogram import Bot, Dispatcher
from handlers import country_handlers, weather_handlers, other_handlers


async def main():
    bot = Bot(token="7854780999:AAFfx3LPcquop89vjIUc4QLIyJhl_vnFgU8")
    dp = Dispatcher()
    dp.include_routers(
        weather_handlers.router,
        country_handlers.router,
        other_handlers.router
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
