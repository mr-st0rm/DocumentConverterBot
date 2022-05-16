import logging

from sqlalchemy.ext.asyncio import AsyncSession
from aiogram import Dispatcher, types

from app.database.models import user as user_db_model


async def user_status_checker(my_chat_member: types.ChatMemberUpdated, session: AsyncSession):
    if my_chat_member.new_chat_member.status == "kicked":
        logging.warning(f"User => {my_chat_member.from_user.id} banned bot")
        await user_db_model.update_user_status(session, my_chat_member.from_user.id, False)
    else:
        logging.warning(f"User => {my_chat_member.from_user.id} started bot")
        await user_db_model.update_user_status(session, my_chat_member.from_user.id, True)


def register_user_status_handler(dp: Dispatcher):
    dp.register_my_chat_member_handler(user_status_checker)

