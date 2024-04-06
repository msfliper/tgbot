from loader import dp
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import messages


@dp.message(F.text == '/start')
async def start(message: types.Message, state: FSMContext):
    await message.answer(messages.WELCOME_MESSAGE)
