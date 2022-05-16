from aiogram import Dispatcher
from sqlalchemy.orm import sessionmaker

from .throtling import ThrottlingMiddleware
from .database_sessions import DBMiddleware


def register_middlewares(dp: Dispatcher, pool: sessionmaker):
    dp.setup_middleware(ThrottlingMiddleware())
    dp.setup_middleware(DBMiddleware(pool))

