import AdminSwitchers
from loader import dp
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import messages, buttons
from States import UserStates
from database.crud.get import get_user
from utils.otchet_utils import send_othcet


@dp.message(UserStates.ADMIN_MENU, F.text == buttons.report_report)
async def otchet(message: types.Message, state: FSMContext):
    await send_othcet(message.from_user.id)
    await AdminSwitchers.admin_menu(message, state)