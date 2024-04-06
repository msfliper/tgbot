from database.db import SessionLocal
from database.models import User, Report
from enums import UserRole, AdvertCreateState


def create_user(telegram_id: int, phone_number: str, username: str) -> User:
    with SessionLocal() as session:
        db_user = User(
            telegram_id=telegram_id,
            phone_number=phone_number,
            username=username,
            role=UserRole.USER
        )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user


def create_report(telegram_id: int, report_text: str) -> Report:
    with SessionLocal() as session:
        db_report = Report(
            telegram_id=telegram_id,
            report_text=report_text,
            create_state=AdvertCreateState.ONLY_TEXT
        )
        session.add(db_report)
        session.commit()
        session.refresh(db_report)
        return db_report
