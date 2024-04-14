import AdminSwitchers
from loader import dp, bot
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import buttons, messages
from States import UserStates
from database.crud.get import get_report
from database.crud.update import report_hire
from enums import ReportAdminStatus
from utils.report_utils import get_current_report_id, get_str_report
from config import settings
from .start import all_reports_start_work


@dp.message(UserStates.ALL_REPORT_IN_WORK, F.text == buttons.next_report)
async def next_report(message: types.Message, state: FSMContext):
    await AdminSwitchers.all_reports_in_work(message, state)


@dp.message(UserStates.ALL_REPORT_IN_WORK, F.text == buttons.report_hire)
async def hire_report(message: types.Message, state: FSMContext):
    report = get_report(await get_current_report_id(state))
    if report.admin_status == ReportAdminStatus.NOT_HIRING:
        report_hire(report.report_id, admin_id=message.from_user.id)
        if report.photo_links:
            await bot.edit_message_caption(caption=get_str_report(report_id=report.report_id),
                                           chat_id=settings.ADMIN_CHAT_ID,
                                           message_id=report.message_id)
        else:
            await bot.edit_message_text(text=get_str_report(report_id=report.report_id),
                                        chat_id=settings.ADMIN_CHAT_ID,
                                        message_id=report.message_id)
        await message.answer(messages.SUCCESSFULLY_GET_REPORT_ALL)
    else:
        await message.answer(messages.ANOTHER_ADMIN_HIRING)
    await AdminSwitchers.all_reports_in_work(message, state)


@dp.message(UserStates.ALL_REPORTS_VIEWED, F.text == buttons.all_reports_again)
async def all_reports_again(message: types.Message, state: FSMContext):
    await all_reports_start_work(message, state)