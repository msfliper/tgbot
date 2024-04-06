from database.db import SessionLocal
from database.models import User
from enums import UserRole


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
