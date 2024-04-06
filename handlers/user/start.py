from loader import dp
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from database.crud.get import get_user
from sqlalchemy.orm.exc import NoResultFound
from view import messages
from UserSwitchers import get_phone_number, main_menu


@dp.message(F.text == '/start')
async def start(message: types.Message, state: FSMContext):
    await message.answer(messages.WELCOME_MESSAGE)
    try:
        get_user(message.from_user.id)
    except NoResultFound:
        await get_phone_number(message, state)
    else:
        await main_menu(message, state)