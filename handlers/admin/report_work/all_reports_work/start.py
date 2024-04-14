import AdminSwitchers
import UserSwitchers
from loader import dp
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import buttons, messages
from States import UserStates
from database.crud.get import get_user, get_report, get_not_hire_reports_id
from sqlalchemy.exc import NoResultFound
from enums import ReportAdminStatus
from utils.report_utils import send_report_to_id


@dp.message(UserStates.REPORT_WORK_CHOICE, F.text == buttons.all_reports)
async def all_reports_start_work(message: types.Message, state: FSMContext):
    all_not_hire_reports = list(reversed(get_not_hire_reports_id()))
    if not all_not_hire_reports:
        await message.answer(messages.NO_NOT_HIRE_REPORT)
        await AdminSwitchers.admin_menu(message, state)
    else:
        all_not_hire_reports_str = '&'.join(list(map(str, all_not_hire_reports)))

        await state.update_data(all_not_hire_reports=all_not_hire_reports_str)
        await AdminSwitchers.all_reports_in_work(message, state)


