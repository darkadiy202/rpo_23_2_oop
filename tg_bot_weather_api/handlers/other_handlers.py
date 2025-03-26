from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from all_keyboards import main_keyboard
from states import UserStates


router = Router()

@router.message(Command("start"))       # /start
async def start(message: types.Message, state: FSMContext):
    await message.answer(
        text="Выберите пункт:",
        reply_markup=main_keyboard()
    )
    await state.set_state(UserStates.user_main_kb)
