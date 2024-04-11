import UserSwitchers
from loader import dp
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import messages, buttons
from States import UserStates
from utils.report_utils import get_current_report_id
from database.crud.get import get_report
from database.crud.delete import delete_report
from enums import ReportCreateState


@dp.message(UserStates.MAIN_MENU, F.text == buttons.create_report_button)
async def create_report(message: types.Message, state: FSMContext):
    await UserSwitchers.create_report(message, state)


@dp.message(F.text == buttons.back_to_main_menu_button)
async def main_menu(message: types.Message, state: FSMContext):
    try:
        report = get_report(await get_current_report_id(state))
    except KeyError:
        pass
    else:
        if report.create_state == ReportCreateState.ONLY_TEXT:
            try:
                delete_report(report.report_id)
            except Exception:
                pass
    await UserSwitchers.main_menu(message, state)
