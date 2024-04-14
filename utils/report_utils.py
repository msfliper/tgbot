from aiogram.fsm.context import FSMContext
from database.crud.get import get_report, get_user
from aiogram.utils.media_group import MediaGroupBuilder
from loader import bot
from datatables import get_admin_status_dict
from typing import List
from view import keyboards


async def get_current_report_id(state: FSMContext) -> int:
    data = await state.get_data()
    return int(data['current_report_id'])


def get_str_report(report_id: int) -> str:
    report = get_report(report_id)
    user = get_user(report.telegram_id)

    str_report = (f"Жалоба от пользователя с ником @{user.username}\n"
                  f"Номер телефона: {user.phone_number}\n\n"
                  f"Коментарий: {report.report_text}\n\n"
                  f"ID: {report.report_id}\n"
                  f"Статус: {get_admin_status_dict()[report.admin_status]}")

    return str_report


async def send_report_to_id(report_id: int, chat_id) -> int:
    report = get_report(report_id)
    user = get_user(report.telegram_id)

    if report.photo_links:
        media_group = MediaGroupBuilder(caption=get_str_report(report_id))
        for photo in report.photo_links.split('&')[:10]:
            media_group.add(type='photo', media=photo)

        msg = await bot.send_media_group(media=media_group.build(),
                                         chat_id=chat_id)
        await bot.send_message(text="Чат в пользователем",
                               reply_markup=keyboards.get_user_contact_button(user.username),
                               chat_id=chat_id)
        return msg[0].message_id

    msg = await bot.send_message(text=get_str_report(report_id),
                                 chat_id=chat_id,
                                 reply_markup=keyboards.get_user_contact_button(user.username))
    return msg.message_id


async def current_not_hire_id(state: FSMContext) -> List[int]:
    data = await state.get_data()
    all_not_hire_reports = data["all_not_hire_reports"]
    print(all_not_hire_reports)
    if (type(all_not_hire_reports) != str) or (all_not_hire_reports == ''):
        return []
    return list(map(int, all_not_hire_reports.split("&")))
