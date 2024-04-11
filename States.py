from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    GET_NUMBER = State()
    MAIN_MENU = State()
    REPORT_TEXT = State()
    REPORT_PHOTO = State()

    ADMIN_MENU = State()
    REPORT_WORK = State()

    REPORT_HIRE = State()
    REPORT_SOLUTION = State()
