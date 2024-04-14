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


@dp.message(UserStates.ADMIN_MENU, F.text == buttons.work_with_reports)
async def report_work_choice(message: types.Message, state: FSMContext):
    await AdminSwitchers.report_work_choice(message, state)


@dp.message(UserStates.REPORT_WORK_CHOICE, F.text == buttons.report_from_id)
async def report_work_from_id(message: types.Message, state: FSMContext):
    await AdminSwitchers.single_report_work(message, state)