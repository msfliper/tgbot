from database.db import SessionLocal
from database.models import User


def get_user(telegram_id: int) -> User:
    with SessionLocal() as session:
        return session.query(User).where(User.telegram_id == telegram_id).one()