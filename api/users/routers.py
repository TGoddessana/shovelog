from typing import Annotated, Any

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.users.schemas import UserListResponse
from config.db import get_session
from api.users.models import User

users_router = APIRouter()


@users_router.get("/", response_model=UserListResponse)
async def get_users(session: Annotated[AsyncSession, Depends(get_session)]) -> Any:
    results = await session.execute(select(User))
    users = results.scalars().all()

    return {"data": users}
