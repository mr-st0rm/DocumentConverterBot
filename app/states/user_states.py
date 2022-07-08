from aiogram.dispatcher.filters.state import StatesGroup, State


class ConverterMenu(StatesGroup):
    choose_from_type = State()
    choose_to_type = State()


class SendDocs(StatesGroup):
    send_file = State()
