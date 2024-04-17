from sqlalchemy import TIMESTAMP, VARCHAR, Column, ForeignKey, Integer, Boolean, TIMESTAMP, BigInteger

from database.db import Base


class User(Base):
    __tablename__ = "users"

    telegram_id = Column(BigInteger, primary_key=True)
    phone_number = Column(VARCHAR)
    username = Column(VARCHAR)
    role = Column(Integer, default=0)


class Report(Base):
    __tablename__ = "reports"

    report_id = Column(Integer, primary_key=True, autoincrement=True)
    telegram_id = Column(BigInteger)
    report_text = Column(VARCHAR)
    photo_links = Column(VARCHAR)
    media_group_id = Column(VARCHAR)
    message_id = Column(VARCHAR)
    create_state = Column(Integer, default=0)
    admin_status = Column(Integer, default=0)
    admin = Column(BigInteger)
    created_at = Column(TIMESTAMP)
    solution_at = Column(TIMESTAMP)
    overdue_message = Column(Boolean, default=False)
    