import sqlalchemy
from sqlalchemy.ext.asyncio import create_async_engine

from app.config.cfg import DatabaseData


def get_engine() -> sqlalchemy.engine.Engine:
    engine: sqlalchemy.engine.Engine = create_async_engine(
        DatabaseData.database_url, encoding="utf-8", echo=False, future=True
    )

    return engine
