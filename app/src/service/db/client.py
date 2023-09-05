"""Database client"""

from contextvars import ContextVar

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
)
from sqlalchemy.orm import sessionmaker

import config
from . import models


db_session_context: ContextVar[AsyncSession] = ContextVar("db_session")

engine = create_async_engine(
    f"postgresql+asyncpg://{config.DB_USER}:{config.DB_PASS}"
    f"@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}",
    echo=True,
)

async_session = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def init_tables():
    """Initializes the database tables."""

    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


def get_session() -> AsyncSession:
    """Returns the session for the current async context."""

    return db_session_context.get()
