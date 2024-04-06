from aiogram import types
from aiogram.fsm.context import FSMContext
from States import UserStates
from view import messages, keyboards


async def get_phone_number(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.GET_NUMBER)
    await message.answer(messages.GET_PHONE_NUMBER)


async def main_menu(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.MAIN_MENU)
    await message.answer(messages.MAIN_MENU,
                         reply_markup=keyboards.get_main_menu_kb())


async def create_report(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.REPORT_TEXT)
    await message.answer(messages.REPORT_TEXT,
                         reply_markup=keyboards.get_back_to_main_menu_kb())


async def get_report_photos(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.REPORT_PHOTO)
    await message.answer(messages.REPORT_PHOTO,
                         reply_markup=keyboards.get_skip_photo_kb())

