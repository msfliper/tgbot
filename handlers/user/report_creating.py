import UserSwitchers
from States import UserStates
from loader import dp
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from database.crud.get import get_user
from sqlalchemy.orm.exc import NoResultFound
from view import messages


@dp.message(UserStates.REPORT_TEXT)
async def get_report_text(message: types.Message, state: FSMContext):
    await state.update_data(report_text=message.text)
    await UserSwitchers.get_report_photos(message, state)
