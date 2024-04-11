from aiogram import types
from aiogram.fsm.context import FSMContext
from States import UserStates
from view import messages, keyboards


async def admin_menu(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.ADMIN_MENU)
    await message.answer(messages.ADMIN_MENU,
                         reply_markup=keyboards.get_admin_menu_kb())


async def report_work(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.REPORT_WORK)
    await message.answer(messages.REPORT_WORK,
                         reply_markup=keyboards.get_back_to_main_menu_kb())


async def report_hire(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.REPORT_HIRE)
    await message.answer(messages.REPORT_HIRE,
                         reply_markup=keyboards.get_report_hire_kb())


async def report_solution(message: types.Message, state: FSMContext):
    await state.set_state(UserStates.REPORT_SOLUTION)
    await message.answer(messages.REPORT_SOLUTION,
                         reply_markup=keyboards.get_report_solution_kb())



