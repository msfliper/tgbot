from typing import List
from database_to_script.models import Report, User
import datetime
from database_to_script.db import SessionLocal
from enums import ReportAdminStatus, UserRole


def get_last_72_hours_reports() -> List[Report]:
    three_days_ago_datatime = datetime.datetime.now() - datetime.timedelta(days=3)
    with SessionLocal() as session:
        return session.query(Report).where(Report.created_at > three_days_ago_datatime).all()


def get_last_24_hours_reports_to_notification() -> List[Report]:
    one_day_ago_datatime = datetime.datetime.now() - datetime.timedelta(days=1)
    with SessionLocal() as session:
        return session.query(Report).where(Report.created_at > one_day_ago_datatime,
                                           Report.admin_status != ReportAdminStatus.REJECT,
                                           Report.admin_status != ReportAdminStatus.RESOLVED,
                                           Report.overdue_message == False).all()


def mark_as_overdue_report_message_send(report_id: int) -> None:
    with SessionLocal() as session:
        session.query(Report).where(Report.report_id == report_id).update({Report.overdue_message: True},
                                                                          synchronize_session=False)
        session.commit()
