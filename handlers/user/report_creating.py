import asyncio

import UserSwitchers
from States import UserStates
from loader import dp
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from utils.report_utils import get_current_report_id
from database.crud.update import (report_add_other_photo, report_add_first_photo,
                                  report_add_one_photo)
from database.crud.create import create_report
from database.crud.get import get_report
from view import messages, buttons


@dp.message(UserStates.REPORT_TEXT)
async def get_report_text(message: types.Message, state: FSMContext):
    if message.photo:
        await message.answer(messages.PHOTO_INSTEAD_OF_TEXT)
        return
    report = create_report(
        telegram_id=message.from_user.id,
        report_text=message.text
    )
    await state.update_data(current_report_id=report.report_id)
    await UserSwitchers.get_report_photos(message, state)


@dp.message(UserStates.REPORT_PHOTO, F.text == buttons.skip_button)
async def skip_photo(message: types.Message, state: FSMContext):
    await UserSwitchers.successful_report(message, state)


@dp.message(UserStates.REPORT_PHOTO)
async def get_report_photos(message: types.Message, state: FSMContext):
    report_id = await get_current_report_id(state)
    report = get_report(report_id)
    if message.media_group_id:
        if report.media_group_id:
            report_add_other_photo(message.photo.pop().file_id, message.media_group_id, report_id)
            return
        report_add_first_photo(message.photo.pop().file_id, message.media_group_id, report_id)
        await asyncio.sleep(0.1)
        await UserSwitchers.successful_report(message, state)

    else:
        if not report.media_group_id:
            report_add_one_photo(message.photo[-1].file_id, report_id)
            await UserSwitchers.successful_report(message, state)
