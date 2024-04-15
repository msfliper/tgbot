import datetime

from database.db import SessionLocal
from database.models import User, Report
from enums import ReportAdminStatus
from typing import List
from datetime import datetime as dt


def get_user(telegram_id: int) -> User:
    with SessionLocal() as session:
        return session.query(User).where(User.telegram_id == telegram_id).one()


def get_report(report_id: int) -> Report:
    with SessionLocal() as session:
        return session.query(Report).where(Report.report_id == report_id).one()


def get_not_hire_reports_id() -> List[int]:
    with SessionLocal() as session:
        return [report.report_id
                for report in session.query(Report).where(Report.admin_status == ReportAdminStatus.NOT_HIRING).all()]


def get_overdue_not_solution_report_id() -> List[int]:
    with SessionLocal() as session:
        return sorted([report.report_id for report in session.query(Report).where(Report.solution_at == None).all()
                       if (dt.now() - report.created_at).days >= 1], )


def get_my_in_work_reports_id(admin_id: int) -> List[int]:
    with SessionLocal() as session:
        return [report.report_id for report in
                session.query(Report).where(Report.admin == admin_id,
                                            Report.admin_status == ReportAdminStatus.IN_WORK).all()]


def get_last_72_hours_reports() -> List[Report]:
    three_days_ago_datatime = datetime.datetime.now() - datetime.timedelta(days=3)
    with SessionLocal() as session:
        return session.query(Report).where(Report.created_at > three_days_ago_datatime).all()


