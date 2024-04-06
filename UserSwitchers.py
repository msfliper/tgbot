from aiogram import types
from aiogram.fsm.context import FSMContext
from States import UserStates
from view import messages


async def get_phone_number(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.GET_NUMBER)
    await message.answer(messages.GET_PHONE_NUMBER)


async def main_menu(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.MAIN_MENU)
    await message.answer(messages.MAIN_MENU)