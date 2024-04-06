import UserSwitchers
from loader import dp
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import messages, buttons
from States import UserStates


@dp.message(UserStates.MAIN_MENU, F.text == buttons.create_report_button)
async def create_report(message: types.Message, state: FSMContext):
    await UserSwitchers.create_report(message, state)


@dp.message(F.text == buttons.back_to_main_menu_button)
async def main_menu(message: types.Message, state: FSMContext):
    await UserSwitchers.main_menu(message, state)