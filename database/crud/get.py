from database.db import SessionLocal
from database.models import User, Report
from enums import ReportAdminStatus
from typing import List


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