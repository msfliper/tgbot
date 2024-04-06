from aiogram.utils.keyboard import (ReplyKeyboardBuilder, InlineKeyboardBuilder,
                                    KeyboardButton, InlineKeyboardButton)
from view import buttons


def get_main_menu_kb() -> ReplyKeyboardBuilder.as_markup:
    main = ReplyKeyboardBuilder()

    main.row(KeyboardButton(text=buttons.create_report_button))

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
