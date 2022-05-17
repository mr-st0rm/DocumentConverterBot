import asyncio
import logging

import sqlalchemy
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.config.cfg import BotData
from app.database import get_engine
from app.database.models import BaseModel
from app.handlers.user import register_user_handlers
from app.middlerware import register_middlewares


async def notify_admins(send_bot: Bot):
    """ Send notify to all admins or no """
    for admin_id in BotData.admins:
        try:
            await send_bot.send_message(chat_id=admin_id, text="Bot started")
        except Exception as e:
            logging.warning(f"\nCan't send start notify to admin -> {admin_id}\n"
                            f"Exception: {e}")


async def init_models():
    """ Create all tables in database """
    engine: sqlalchemy.engine.Engine = get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


async def register_all_dependencies(dsp: Dispatcher, db_pool: sessionmaker):
    """ Register middlewares """
    register_middlewares(dsp, db_pool)

    # Register user handlers
    register_user_handlers(dsp)

    # Register admin handlers


async def main():
    bot = Bot(BotData.bot_token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Get engine
    engine = get_engine()
    db_pool = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    # Create db tables
    await init_models()

    await register_all_dependencies(dp, db_pool)
    await notify_admins(bot)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        bot_session = await bot.get_session()
        await bot_session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error("Bot stopped!")
