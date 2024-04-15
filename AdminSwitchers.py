from aiogram import types
from aiogram.fsm.context import FSMContext
from States import UserStates
from view import messages, keyboards
from utils.report_utils import current_not_hire_id, send_report_to_id


async def admin_menu(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.ADMIN_MENU)
    await message.answer(messages.ADMIN_MENU,
                         reply_markup=keyboards.get_admin_menu_kb())


async def report_work_choice(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.REPORT_WORK_CHOICE)
    await message.answer(messages.REPORT_WORK_CHOICE,
                         reply_markup=keyboards.get_report_work_choice_kb())


async def single_report_work(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.SINGLE_REPORT_WORK)
    await message.answer(messages.GET_SINGLE_REPORT_ID,
                         reply_markup=keyboards.get_back_to_main_menu_kb())


async def report_hire(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.REPORT_HIRE)
    await message.answer(messages.REPORT_HIRE,
                         reply_markup=keyboards.get_report_hire_kb())


async def report_solution(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.REPORT_SOLUTION)
    await message.answer(messages.REPORT_SOLUTION,
                         reply_markup=keyboards.get_report_solution_kb())


async def all_reports_in_work(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.ALL_REPORT_IN_WORK)
    current_admin_ids = await current_not_hire_id(state)

    if current_admin_ids:
        report_id = current_admin_ids.pop()
        await state.update_data(all_not_hire_reports='&'.join(list(map(str, current_admin_ids))),
                                current_report_id=report_id)
        await send_report_to_id(report_id=report_id,
                                chat_id=message.from_user.id)
        await message.answer(messages.ALL_REPORTS_ACTION_CHOICE,
                             reply_markup=keyboards.get_all_reports_action_kb())
    else:
        await all_repost_viewed(message, state)


async def all_repost_viewed(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.ALL_REPORTS_VIEWED)
    await message.answer(messages.ALL_REPORTS_VIEWED,
                         reply_markup=keyboards.get_all_report_viewed_choice_kb())


async def choice_report_list(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.CHOICE_REPORT_LIST)
    await message.answer(messages.CHOICE_REPORT_LIST,
                         reply_markup=keyboards.get_choice_report_list_kb())
