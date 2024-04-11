from aiogram.utils.keyboard import (ReplyKeyboardBuilder, InlineKeyboardBuilder,
                                    KeyboardButton, InlineKeyboardButton)
from view import buttons


def get_main_menu_kb() -> ReplyKeyboardBuilder.as_markup:
    main = ReplyKeyboardBuilder()

    main.row(KeyboardButton(text=buttons.create_report_button))

    return main.as_markup(resize_keyboards=True)


def get_main_menu_admin_kb() -> ReplyKeyboardBuilder.as_markup:
    main = ReplyKeyboardBuilder()

    main.row(KeyboardButton(text=buttons.create_report_button))
    main.row(KeyboardButton(text=buttons.to_admin_menu))

    return main.as_markup(resize_keyboards=True)


def get_back_to_main_menu_kb() -> ReplyKeyboardBuilder.as_markup:
    back_to_mm = ReplyKeyboardBuilder()

    back_to_mm.row(KeyboardButton(text=buttons.back_to_main_menu_button))

    return back_to_mm.as_markup(resize_keyboards=True)


def get_skip_photo_kb() -> ReplyKeyboardBuilder.as_markup:
    skip_photo = ReplyKeyboardBuilder()

    skip_photo.row(KeyboardButton(text=buttons.skip_button))
    skip_photo.row(KeyboardButton(text=buttons.back_to_main_menu_button))

    return skip_photo.as_markup()


def get_admin_menu_kb() -> ReplyKeyboardBuilder.as_markup:
    admin_menu = ReplyKeyboardBuilder()

    admin_menu.row(KeyboardButton(text=buttons.report_work))
    admin_menu.row(KeyboardButton(text=buttons.report_list))
    admin_menu.row(KeyboardButton(text=buttons.back_to_main_menu_button))

    return admin_menu.as_markup()


def get_report_hire_kb() -> ReplyKeyboardBuilder.as_markup:
    report_hire = ReplyKeyboardBuilder()

    report_hire.row(KeyboardButton(text=buttons.report_hire))
    report_hire.row(KeyboardButton(text=buttons.back_to_main_menu_button))

    return report_hire.as_markup()


def get_report_solution_kb() -> ReplyKeyboardBuilder.as_markup:
    report_solution = ReplyKeyboardBuilder()

    report_solution.row(KeyboardButton(text=buttons.report_solution))
    report_solution.row(KeyboardButton(text=buttons.back_to_main_menu_button))

    return report_solution.as_markup()
