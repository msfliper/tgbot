from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    GET_NUMBER = State()
    MAIN_MENU = State()
    REPORT_TEXT = State()
    REPORT_PHOTO = State()

    ADMIN_MENU = State()
    REPORT_WORK_CHOICE = State()

    SINGLE_REPORT_WORK = State()
    REPORT_HIRE = State()
    REPORT_SOLUTION = State()
    ALL_REPORT_IN_WORK = State()
    ALL_REPORTS_VIEWED = State()

    CHOICE_REPORT_LIST = State()
