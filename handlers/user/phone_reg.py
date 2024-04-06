from loader import dp
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from view import messages
from UserSwitchers import get_phone_number, main_menu
from States import UserStates
from database.crud.create import create_user


@dp.message(UserStates.GET_NUMBER)
async def get_number(message: types.Message, state: FSMContext):
    if len(message.text) == 12:
        try:
            int(message.text.replace("+",""))
        except ValueError:
            await message.answer(messages.WRONG_PHONE_NUMBER_FORMAT)
            await get_phone_number(message, state)
        else:
            create_user(telegram_id=message.from_user.id,
                        phone_number=message.text,
                        username=message.from_user.username)
            await message.answer(messages.SUCCESSFUL_PHONE_REGISTRATION)
            await main_menu(message, state)

    else:
        await message.answer(messages.WRONG_PHONE_NUMBER_FORMAT)
        await get_phone_number(message, state)