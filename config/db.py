from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from config.settings import settings

DB_URL: str = settings.db_url

engine = create_async_engine(DB_URL, echo=True)
metadata = SQLModel.metadata
