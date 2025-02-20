from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from users import user_service

from db.database import get_session
from modules.oauth2_scheme import get_user_id

router = APIRouter(prefix="/users")


@router.get('/my')
def get_my_profile(
    user_id: str = Depends(get_user_id),
    db: Session = Depends(get_session),
):
    return user_service.get_profile(user_id=user_id, db=db)