from database.db import SessionLocal
from database.models import User, Report
from enums import ReportCreateState, ReportAdminStatus, UserRole
import datetime


def report_add_one_photo(photo_link: str, report_id: int):
    with SessionLocal() as session:
        session.query(Report).where(Report.report_id == report_id).update({Report.photo_links: photo_link},
                                                                          synchronize_session=False)
        session.commit()


def report_add_first_photo(photo_link: str, media_group_id: str, report_id: int):
    with SessionLocal() as session:
        session.query(Report).where(Report.report_id == report_id).update({Report.photo_links: photo_link,
                                                                           Report.media_group_id: media_group_id},
                                                                          synchronize_session=False)
        session.commit()


def report_add_other_photo(photo_link: str, media_group_id: str, report_id: int):
    with SessionLocal() as session:
        old_links = session.query(Report).where(
            (Report.report_id == report_id) and (Report.media_group_id == media_group_id)).one().photo_links
        new_links = f'{old_links}&{photo_link}'
        session.query(Report).where((Report.report_id == report_id) and (Report.media_group_id == media_group_id)). \
            update({Report.photo_links: new_links},
                   synchronize_session=False)
        session.commit()


def report_set_finished_status(report_id: int, message_id: int):
    with SessionLocal() as session:
        session.query(Report).where(Report.report_id == report_id).update({Report.create_state:
                                                                               ReportCreateState.FINISHED,
                                                                           Report.created_at: datetime.datetime.now(),
                                                                           Report.message_id: message_id},
                                                                          synchronize_session=False)
        session.commit()


def report_hire(report_id: int, admin_id: int):
    with SessionLocal() as session:
        session.query(Report).where(Report.report_id == report_id).update({Report.admin: admin_id,
                                                                           Report.admin_status:
                                                                           ReportAdminStatus.IN_WORK},
                                                                          synchronize_session=False)
        session.commit()


def report_reject(report_id: int):
    with SessionLocal() as session:
        session.query(Report).where(Report.report_id == report_id).update({Report.admin_status:
                                                                           ReportAdminStatus.REJECT},
                                                                          synchronize_session=False)
        session.commit()


def report_solution(report_id: int):
    with SessionLocal() as session:
        session.query(Report).where(Report.report_id == report_id).update({Report.admin_status:
                                                                               ReportAdminStatus.RESOLVED,
                                                                           Report.solution_at: datetime.datetime.now()},
                                                                          synchronize_session=False)
        session.commit()


def user_to_administrator(telegram_id: int):
    with SessionLocal() as session:
        session.query(User).where(User.telegram_id == telegram_id).update({User.role: UserRole.ADMIN},
                                                                           synchronize_session=False)
        session.commit()