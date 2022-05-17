from aiogram import Dispatcher
from sqlalchemy.orm import sessionmaker

from .database_sessions import DBMiddleware
from .throtling import ThrottlingMiddleware


def register_middlewares(dp: Dispatcher, pool: sessionmaker):
    dp.setup_middleware(DBMiddleware(pool))
    dp.setup_middleware(ThrottlingMiddleware())

