import AdminSwitchers
import UserSwitchers
from loader import dp, bot
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import buttons, messages
from States import UserStates
from database.crud.get import get_user, get_report
from database.crud.update import report_solution
from utils.report_utils import report_message_refresh, get_current_report_id, get_str_report
from config import settings


@dp.message(UserStates.REPORT_SOLUTION, F.text == buttons.report_solution)
async def report_solution_yes(message: types.Message, state: FSMContext):
    report = get_report(await get_current_report_id(state))
    report_solution(report_id=report.report_id)
    await message.answer(messages.SUCCESSFULLY_SOLUTION)
    await report_message_refresh(report)
    await UserSwitchers.main_menu(message, state)