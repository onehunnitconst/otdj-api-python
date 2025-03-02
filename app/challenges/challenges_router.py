from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.challenges.dto.update_challenge_dto import UpdateChallengeDto
from modules.oauth2_scheme import get_user_id
from db.database import get_session

from .dto.create_challenge_dto import CreateChallengeDto
from .challenges_service import get_my_todos

router = APIRouter(prefix="/todos")


@router.get("/")
def get_challenges(
    user_id: str = Depends(get_user_id),
    db: Session = Depends(get_session),
):
    return get_my_todos(user_id, db)


@router.post("/")
def create_challenge(
    body: CreateChallengeDto,
    user_id: str = Depends(get_user_id),
    db: Session = Depends(get_session),
):
    return get_my_todos(user_id=user_id, body=body, db=db)

@router.patch("/{challenge_id}")
def update_challenge(
    challenge_id: int,
    body: UpdateChallengeDto,
    user_id: str = Depends(get_user_id),
    db: Session = Depends(get_session),
):
    return update_challenge(
        user_id=user_id,
        challenge_id=challenge_id,
        body=body,
        db=db,
    )

@router.delete("/{challenge_id}")
def delete_challenge(
    challenge_id: int,
    user_id: str = Depends(get_user_id),
    db: Session = Depends(get_session),
):
    return delete_challenge(challenge_id, user_id, db)