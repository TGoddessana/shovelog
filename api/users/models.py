from datetime import datetime
from enum import Enum as PythonEnum

from sqlalchemy import Column, Integer, String, Boolean, DateTime, Enum

from config.db import Model


class UserRole(str, PythonEnum):
    ADMIN = "admin"
    EDITOR = "editor"
    READER = "reader"


class User(Model):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    is_active = Column(Boolean(), default=False)
    role = Column(Enum(UserRole), default=UserRole.READER)
