import logging

import sqlalchemy
from aiogram import Dispatcher, Bot
from aiogram import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.database.models import BaseModel
from app.middlerware import register_middlewares
from app.config.cfg import BotData, DatabaseData
from app.handlers.user import register_user_handlers


bot = Bot(BotData.bot_token)
dp = Dispatcher(bot, storage=MemoryStorage())


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
    engine: sqlalchemy.engine.Engine = create_async_engine(
        DatabaseData.database_url, encoding="utf-8", echo=False, future=True
    )
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


async def register_all_dependencies(dsp: Dispatcher, db_pool: sessionmaker):
    """ Register middlewares """
    register_middlewares(dsp, db_pool)

    # Register user handlers
    register_user_handlers(dp)

    # Register admin handlers


async def main(dsp: Dispatcher):
    # Creating DB engine for PostgreSQL
    engine: sqlalchemy.engine.Engine = create_async_engine(
        DatabaseData.database_url, encoding="utf-8", echo=False, future=True
    )

    # Creating DB connections pool
    db_pool = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    await init_models()
    await register_all_dependencies(dsp, db_pool)
    await notify_admins(bot)


if __name__ == "__main__":
    executor.start_polling(dp, on_startup=main)
