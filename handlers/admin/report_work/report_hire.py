import UserSwitchers
from loader import dp, bot
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import buttons, messages
from States import UserStates
from database.crud.get import get_user, get_report
from database.crud.update import report_hire
from utils.report_utils import send_report_to_id, get_current_report_id, get_str_report
from config import settings


@dp.message(UserStates.REPORT_HIRE, F.text == buttons.report_hire)
async def report_hire_yes(message: types.Message, state: FSMContext):
    report = get_report(await get_current_report_id(state))
    report_hire(report.report_id, message.from_user.id)
    await message.answer(messages.SUCCESSFULLY_HIRE)
    if report.photo_links:
        await bot.edit_message_caption(caption=get_str_report(report_id=report.report_id),
                                       chat_id=settings.ADMIN_CHAT_ID,
                                       message_id=report.message_id)
    else:
        await bot.edit_message_text(text=get_str_report(report_id=report.report_id),
                                    chat_id=settings.ADMIN_CHAT_ID,
                                    message_id=report.message_id)
    await UserSwitchers.main_menu(message, state)