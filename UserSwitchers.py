from aiogram import types
from aiogram.fsm.context import FSMContext
from States import UserStates
from view import messages, keyboards
from database.crud.update import report_set_finished_status
from database.crud.get import get_user, get_report
from utils.report_utils import get_current_report_id, send_report_to_id
from config import settings
from enums import UserRole


async def get_phone_number(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.GET_NUMBER)
    await message.answer(messages.GET_PHONE_NUMBER)


async def main_menu(message: types.Message, state: FSMContext):
    if get_user(message.from_user.id).role == UserRole.USER:
        await state.set_state(UserStates.MAIN_MENU)
        await message.answer(messages.MAIN_MENU,
                             reply_markup=keyboards.get_main_menu_kb())
        return
    else:
        await state.set_state(UserStates.ADMIN_MENU)
        await message.answer(messages.ADMIN_MENU,
                             reply_markup=keyboards.get_admin_menu_kb())


async def create_report(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.REPORT_TEXT)
    await message.answer(messages.REPORT_TEXT,
                         reply_markup=keyboards.get_back_to_main_menu_kb())


async def get_report_photos(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.REPORT_PHOTO)
    await message.answer(messages.REPORT_PHOTO,
                         reply_markup=keyboards.get_skip_photo_kb())


async def successful_report(message: types.Message, state: FSMContext):
    await message.answer(messages.SUCCESSFUL_REPORT_CREATE)
    report_id = await get_current_report_id(state)
    message_id = await send_report_to_id(report_id, settings.ADMIN_CHAT_ID)
    report_set_finished_status(report_id, message_id)
    await main_menu(message, state)
