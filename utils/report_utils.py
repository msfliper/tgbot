import datetime

from aiogram.fsm.context import FSMContext
from database.crud.get import get_report, get_user
from aiogram.utils.media_group import MediaGroupBuilder
from loader import bot
from datatables import get_admin_status_dict
from typing import List
from view import keyboards
from database.models import Report
from config import settings

async def get_current_report_id(state: FSMContext) -> int:
    data = await state.get_data()
    return int(data['current_report_id'])


def get_str_report(report_id: int) -> str:
    report = get_report(report_id)
    user = get_user(report.telegram_id)

    if not report.created_at:
        current_datatime = datetime.datetime.now() + datetime.timedelta(days=1)
    else:
        current_datatime = report.created_at + datetime.timedelta(days=1)
    str_report = (f"Жалоба от пользователя с ником @{user.username}\n"
                  f"Номер телефона: {user.phone_number}\n\n"
                  f"Коментарий: {report.report_text}\n\n"
                  f"ID: {report.report_id}\n"
                  f"Статус: {get_admin_status_dict()[report.admin_status]}\n\n"
                  f"Обработать до {current_datatime.day}.{current_datatime.month} | "
                  f"{current_datatime.hour}:{current_datatime.minute}")

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
        await bot.send_message(text="Чат с пользователем",
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
    if (type(all_not_hire_reports) != str) or (all_not_hire_reports == ''):
        return []
    return list(map(int, all_not_hire_reports.split("&")))


async def report_message_refresh(report: Report) -> None:
    if report.photo_links:
        await bot.edit_message_caption(caption=get_str_report(report_id=report.report_id),
                                       chat_id=settings.ADMIN_CHAT_ID,
                                       message_id=report.message_id)
    else:
        await bot.edit_message_text(text=get_str_report(report_id=report.report_id),
                                    chat_id=settings.ADMIN_CHAT_ID,
                                    message_id=report.message_id)


def get_overdue_report_list_message(reports_id: List[int]) -> str:
    if reports_id:
        return f"Список просроченых жалоб: {', '.join(map(str, reports_id))}"
    return f"В данный момент, просроченых жалоб нет"


def get_my_in_work_report_list_message(reports_id: List[int]) -> str:
    if reports_id:
        return f"Список жалоб, взятых вами в работу: {', '.join(map(str, reports_id))}"
    return f"В данный момент у вас в работе нет ни одной жалобы"


def get_not_hire_reports_message(reports_id: List[int]) -> str:
    if reports_id:
        return f"Список жалоб, никем не взятых в работу: {', '.join(map(str, reports_id))}"
    return f"В данный момент нет жалоб, которые можно было бы взять в работу"
