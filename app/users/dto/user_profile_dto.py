from typing import Optional
from pydantic import BaseModel


class UserProfileDto(BaseModel):
    id: int
    user_id: str
    nickname: str
    profile_image: Optional[str]