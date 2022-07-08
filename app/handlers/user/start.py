import html

from aiogram import Dispatcher
from aiogram import types
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models import user as user_model
from app.keyboards.reply import user_reply as user_r_kb
from app.messages.user import start_msgs


async def welcome_user(message: types.Message, session: AsyncSession):
    """ Wellcome and add register user """
    if not await user_model.get_user(session, message.from_user.id):
        await user_model.registrate_user(session, message.from_user.id, message.from_user.username,
                                         message.from_user.full_name)
    await message.answer(start_msgs.welcome_user(html.escape(message.from_user.full_name)),
                         reply_markup=user_r_kb.bot_main_keyboard())


def register_start_handler(dp: Dispatcher):
    dp.register_message_handler(welcome_user, commands=['start'], state="*")
