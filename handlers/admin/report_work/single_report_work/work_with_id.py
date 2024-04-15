import AdminSwitchers
import UserSwitchers
from loader import dp
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import buttons, messages
from States import UserStates
from database.crud.get import get_user, get_report
from sqlalchemy.exc import NoResultFound
from enums import ReportAdminStatus
from utils.report_utils import send_report_to_id


@dp.message(UserStates.SINGLE_REPORT_WORK)
async def get_report_id(message: types.Message, state: FSMContext):
    try:
        report = get_report(int(message.text))
    except (NoResultFound, ValueError):
        await message.answer(messages.WRONG_REPORT_ID)
    else:
        if report.admin_status == ReportAdminStatus.NOT_HIRING:
            await send_report_to_id(report.report_id, message.from_user.id)
            await state.update_data(current_report_id=report.report_id)
            await AdminSwitchers.report_hire(message, state)

        elif report.admin_status == ReportAdminStatus.IN_WORK:
            if message.from_user.id != report.admin:
                await message.answer(messages.ANOTHER_ADMIN_HIRING_OR_REJECT)
                await UserSwitchers.main_menu(message, state)
                return

            await send_report_to_id(report.report_id, message.from_user.id)
            await state.update_data(current_report_id=report.report_id)
            await AdminSwitchers.report_solution(message, state)

        else:
            await message.answer(messages.ALREADY_SOLUTION_OR_REJECT)
            await UserSwitchers.main_menu(message, state)
