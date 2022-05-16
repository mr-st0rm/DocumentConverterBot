import typing

from sqlalchemy import Column, String, BigInteger, Boolean, DateTime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.sql import func
from sqlalchemy.engine import CursorResult

from app.database.models import BaseModel


class User(BaseModel):
    """ Users table """
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id = Column(BigInteger, unique=True)
    user_username = Column(String(32))
    user_fullname = Column(String(64))
    user_status = Column(Boolean, default=True)
    reg_date = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return f"User\n{self.id}\n{self.user_id=}\n{self.user_username=}\n{self.user_fullname}\n" \
               f"{self.user_status}\n{self.reg_date}"


async def get_user(session: AsyncSession, user_id: int) -> typing.Optional[User]:
    """ Get all information about user or empty tuple"""
    select_query = select(User).where(User.user_id == user_id)
    result: CursorResult = await session.execute(select_query)

    return result.scalars().first()


async def registrate_user(session: AsyncSession, user_id: int, username: str, user_fullname: str):
    """ Adding a new user to database, if the user is already in the database, do nothing """
    user = User(
        user_id=user_id,
        user_username=username,
        user_fullname=user_fullname
    )
    session.add(user)

    await session.commit()


async def update_user_status(session: AsyncSession, user_id: int, status: bool):
    """ Updating user status, if user start bot or stop it """

    user: User = await get_user(session, user_id)
    user.user_status = status

    await session.commit()
