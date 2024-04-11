from database.db import SessionLocal
from database.models import User, Report


def delete_report(report_id: int) -> None:
    with SessionLocal() as session:
        session.query(Report).where(Report.report_id == report_id).delete()
        session.commit()