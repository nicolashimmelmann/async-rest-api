"""Declarations of database models"""

from typing import Any

from sqlalchemy.types import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True, nullable=False, autoincrement=True
    )
    username: Mapped[str] = mapped_column(
        String(32), nullable=False, unique=True
    )
