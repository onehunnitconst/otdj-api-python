from sqlalchemy.orm import Session

from users.dto.user_profile_dto import UserProfileDto
from db.models import User


def get_profile(db: Session, user_id: str):
    user = db.query(User).where(User.id == user_id).first()

    return UserProfileDto(
        id=user.id,
        user_id=user.user_id,
        nickname=user.nickname,
        profile_image=user.profile_image,
    )
