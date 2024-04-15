import AdminSwitchers
from loader import dp, bot
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import buttons, messages
from States import UserStates
from database.crud.get import get_report
from database.crud.update import report_hire, report_reject
from enums import ReportAdminStatus
from utils.report_utils import get_current_report_id, report_message_refresh
from .start import all_reports_start_work


@dp.message(UserStates.ALL_REPORT_IN_WORK, F.text == buttons.next_report)
async def next_report(message: types.Message, state: FSMContext):
    await AdminSwitchers.all_reports_in_work(message, state)


@dp.message(UserStates.ALL_REPORT_IN_WORK, F.text == buttons.report_hire)
async def hire_report(message: types.Message, state: FSMContext):
    report = get_report(await get_current_report_id(state))
    if report.admin_status == ReportAdminStatus.NOT_HIRING:
        report_hire(report.report_id, admin_id=message.from_user.id)
        await report_message_refresh(report)
        await message.answer(messages.SUCCESSFULLY_GET_REPORT_ALL)
    else:
        await message.answer(messages.ANOTHER_ADMIN_HIRING_OR_REJECT)
    await AdminSwitchers.all_reports_in_work(message, state)


@dp.message(UserStates.ALL_REPORT_IN_WORK, F.text == buttons.report_reject)
async def reject_report(message: types.Message, state: FSMContext):
    report = get_report(await get_current_report_id(state))
    if report.admin_status == ReportAdminStatus.NOT_HIRING:
        report_reject(report.report_id)
        await report_message_refresh(report)
        await message.answer(messages.REPORT_REJECT)
    else:
        await message.answer(messages.ANOTHER_ADMIN_HIRING_OR_REJECT)
    await AdminSwitchers.all_reports_in_work(message, state)


@dp.message(UserStates.ALL_REPORTS_VIEWED, F.text == buttons.all_reports_again)
async def all_reports_again(message: types.Message, state: FSMContext):
    await all_reports_start_work(message, state)