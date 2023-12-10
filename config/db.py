from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel import SQLModel
from config.settings import settings


engine = create_async_engine(settings.DB_URL, echo=True)
metadata = SQLModel.metadata
