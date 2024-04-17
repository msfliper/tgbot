import asyncio
import datetime

from loader import bot
from database_to_script.crud import get_last_24_hours_reports_to_notification, mark_as_overdue_report_message_send
from config import settings
from view import messages


async def main():
    reports = get_last_24_hours_reports_to_notification()
    reports = [report for report in reports
               if (datetime.datetime.now()-report.created_at).seconds//3600 >= 12]
    for report in reports:
        await bot.send_message(reply_to_message_id=report.message_id,
                               chat_id=settings.ADMIN_CHAT_ID,
                               text=messages.OVERDUE_REPORT)
        mark_as_overdue_report_message_send(report.report_id)


asyncio.run(main())
