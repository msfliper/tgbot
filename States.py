from aiogram.fsm.state import StatesGroup, State


class UserStates(StatesGroup):
    GET_NUMBER = State()
    MAIN_MENU = State()
    REPORT_TEXT = State()
    REPORT_PHOTO = State()