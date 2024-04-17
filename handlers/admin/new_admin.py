import AdminSwitchers
from loader import dp
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import messages, buttons
from States import UserStates
from database.crud.get import get_user_from_phone, get_user
from database.crud.update import user_to_administrator
from enums import UserRole


@dp.message(UserStates.ADMIN_MENU, F.text == buttons.new_admin)
async def new_admin(message: types.Message, state: FSMContext):
    if get_user(message.from_user.id).role == UserRole.USER:
        return
    await AdminSwitchers.new_admin(message, state)


@dp.message(UserStates.NEW_ADMIN)
async def get_new_admin_phone(message: types.Message, state: FSMContext):
    if len(message.text) == 12:
        try:
            int(message.text.replace("+", ""))
        except ValueError:
            await message.answer(messages.WRONG_PHONE_NUMBER_FORMAT)
        else:
            try:
                user = get_user_from_phone(message.text)
            except Exception:
                await message.answer(messages.NO_USERS_WITH_PHONE)
            else:
                user_to_administrator(user.telegram_id)
                await message.answer(messages.SUCCESSFULLY_NEW_ADMIN)
                await AdminSwitchers.admin_menu(message, state)
                