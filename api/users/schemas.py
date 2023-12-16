from datetime import datetime
from typing import Sequence

from pydantic import BaseModel, EmailStr


class UserListResponse(BaseModel):
    class _User(BaseModel):
        id: int
        username: str
        email: EmailStr
        is_active: bool
        created_at: datetime
        role: str

    data: Sequence[_User]
