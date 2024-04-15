import UserSwitchers
from loader import dp, bot
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import buttons, messages
from States import UserStates
from database.crud.get import get_user, get_report
from database.crud.update import report_hire, report_reject
from utils.report_utils import report_message_refresh, get_current_report_id, get_str_report
from config import settings


@dp.message(UserStates.REPORT_HIRE, F.text == buttons.report_hire)
async def report_hire_yes(message: types.Message, state: FSMContext):
    report = get_report(await get_current_report_id(state))
    report_hire(report.report_id, message.from_user.id)
    await message.answer(messages.SUCCESSFULLY_HIRE)
    await report_message_refresh(report)
    await UserSwitchers.main_menu(message, state)


@dp.message(UserStates.REPORT_HIRE, F.text == buttons.report_reject)
async def report_reject_yes(message: types.Message, state: FSMContext):
    report = get_report(await get_current_report_id(state))
    report_reject(report.report_id)
    await message.answer(messages.REPORT_REJECT)
    await report_message_refresh(report)
    await UserSwitchers.main_menu(message, state)