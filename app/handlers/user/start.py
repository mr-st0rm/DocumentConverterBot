from aiogram import Dispatcher
from aiogram import types

from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import user as user_model
from app.keyboards.reply import user_reply as user_r_kb


async def welcome_user(message: types.Message, session: AsyncSession):
    """ Wellcome and add user into database """
    await user_model.registrate_user(session, message.from_user.id, message.from_user.username,
                                     message.from_user.full_name)
    await message.answer(f"Привет, {message.from_user.full_name}\n"
                         f"Я могу конвертировать документа разных форматов.",
                         reply_markup=user_r_kb.bot_main_keyboard())


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(welcome_user, commands=['start'])
