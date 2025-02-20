from typing import Optional
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base

class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str]
    password: Mapped[str]
    nickname: Mapped[str]
    profile_image: Mapped[Optional[str]]
