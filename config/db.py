from asyncio import current_task

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
)
from sqlalchemy.orm import declarative_base
from config.settings import settings


engine = create_async_engine(
    settings.DB_URL, echo=True, connect_args={"check_same_thread": False}
)

async_session_factory = async_sessionmaker(engine, class_=AsyncSession)

AsyncSession = async_scoped_session(async_session_factory, scopefunc=current_task)

naming_convention = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}

Model = declarative_base(metadata=MetaData(naming_convention=naming_convention))
