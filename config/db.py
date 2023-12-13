from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base

from config.settings import settings


engine = create_async_engine(
    settings.DB_URL,
    echo=True,
)

Model = declarative_base()
