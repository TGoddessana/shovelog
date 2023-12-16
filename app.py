from fastapi import FastAPI

from api.users.routers import users_router
from config.settings import settings


app = FastAPI(
    title=settings.TITLE,
    description=settings.DESCRIPTION,
)

app.include_router(users_router)
