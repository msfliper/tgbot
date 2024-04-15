from aiogram import F, types
from aiogram.fsm.context import FSMContext

import AdminSwitchers
from States import UserStates
from database.crud.get import get_overdue_not_solution_report_id, get_my_in_work_reports_id, get_not_hire_reports_id
from loader import dp
from utils.report_utils import get_overdue_report_list_message, get_my_in_work_report_list_message, get_not_hire_reports_message
from view import buttons


@dp.message(UserStates.ADMIN_MENU, F.text == buttons.reports_list)
async def reports_list(message: types.Message, state: FSMContext):
    await AdminSwitchers.choice_report_list(message, state)


@dp.message(UserStates.CHOICE_REPORT_LIST, F.text == buttons.overdue_reports)
async def overdue_reports_list(message: types.Message, state: FSMContext):
    reports_id = get_overdue_not_solution_report_id()
    await message.answer(get_overdue_report_list_message(reports_id))
    await AdminSwitchers.admin_menu(message, state)


@dp.message(UserStates.CHOICE_REPORT_LIST, F.text == buttons.my_in_work)
async def my_in_work_list(message: types.Message, state: FSMContext):
    reports_id = get_my_in_work_reports_id(message.from_user.id)
    await message.answer(get_my_in_work_report_list_message(reports_id))
    await AdminSwitchers.admin_menu(message, state)


@dp.message(UserStates.CHOICE_REPORT_LIST, F.text == buttons.all_not_hire)
async def all_not_hire(message: types.Message, state: FSMContext):
    reports_id = get_not_hire_reports_id()
    await message.answer(get_not_hire_reports_message(reports_id))
    await AdminSwitchers.admin_menu(message, state)


