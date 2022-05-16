from aiogram import Dispatcher


from .convert_menu import register_converter_handlers
from .start import register_start_handler
from .user_links import register_links_handler
from .user_status import register_user_status_handler


def register_user_handlers(dp: Dispatcher):
    register_start_handler(dp)
    register_converter_handlers(dp)
    register_links_handler(dp)
    register_user_status_handler(dp)
