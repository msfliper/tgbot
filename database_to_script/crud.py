from typing import List
from database_to_script.models import Report
import datetime
from database_to_script.db import SessionLocal


def get_last_72_hours_reports() -> List[Report]:
    three_days_ago_datatime = datetime.datetime.now() - datetime.timedelta(days=3)
    with SessionLocal() as session:
        return session.query(Report).where(Report.created_at > three_days_ago_datatime).all()