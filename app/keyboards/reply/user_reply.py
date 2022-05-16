from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def bot_main_keyboard() -> ReplyKeyboardMarkup:
    """ Generate main bot`s reply keyboard """
    result_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
        [KeyboardButton("🔄 Конвертировать файл")],
        [KeyboardButton("Инструкция"), KeyboardButton("💬 Ссылки")]
    ])

    return result_kb
