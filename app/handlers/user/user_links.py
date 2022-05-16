from aiogram import Dispatcher
from aiogram import types
from aiogram.dispatcher.filters import Text

from app.keyboards.inline.user_inline import user_links


async def info_links(message: types.Message):
    """ All links for users """
    await message.answer("Все нужные ссылки ты можешь найти ниже",
                         reply_markup=user_links())


def register_links_handler(dp: Dispatcher):
    dp.register_message_handler(info_links, Text("💬 Ссылки"), state="*")
