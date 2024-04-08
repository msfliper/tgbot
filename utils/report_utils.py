from aiogram.fsm.context import FSMContext
from aiogram import types
from database.crud.get import get_report, get_user
from aiogram.utils.media_group import MediaGroupBuilder
from loader import bot


async def get_current_report_id(state: FSMContext) -> int:
    data = await state.get_data()
    return int(data['current_report_id'])


def get_str_report(report_id: int) -> str:
    report = get_report(report_id)
    user = get_user(report.telegram_id)

    str_report = (f"Жалоба от пользователя с ником @{user.username}\n"
                  f"Номер телефона: {user.phone_number}\n\n"
                  f"Коментарий: {report.report_text}")

    return str_report


async def send_report_to_id(report_id: int, chat_id) -> int:
    report = get_report(report_id)

    if report.photo_links:
        media_group = MediaGroupBuilder(caption=get_str_report(report_id))
        for photo in report.photo_links.split('&')[:10]:
            media_group.add(type='photo', media=photo)

        msg = await bot.send_media_group(media=media_group.build(),
                                         chat_id=chat_id)
        return msg[0].message_id

    msg = await bot.send_message(text=get_str_report(report_id),
                                 chat_id=chat_id)
    return msg.message_id
