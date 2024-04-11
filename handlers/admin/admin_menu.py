import AdminSwitchers
from loader import dp
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import messages, buttons
from States import UserStates
from database.crud.get import get_user
from enums import UserRole


@dp.message(UserStates.MAIN_MENU, F.text == buttons.to_admin_menu)
async def admin_menu(message: types.Message, state: FSMContext):
    if get_user(message.from_user.id).role == UserRole.USER:
        return
    await AdminSwitchers.admin_menu(message, state)
