from datetime import datetime
from fastapi import HTTPException
from sqlalchemy.orm import Session

from db.models import Challenge
from .dto.create_challenge_dto import CreateChallengeDto
from .dto.challenge_dto import ChallengeDto
from .dto.update_challenge_dto import UpdateChallengeDto


def create_challenge(user_id: str, body: CreateChallengeDto, db: Session):
    new_challenge = Challenge(
        user_id=user_id,
        song_id=body.song_id,
        chart_id=body.chart_id,
        challenge_type=body.challenge_type,
        challenge_goal=body.challenge_goal,
    )

    db.add(new_challenge)
    db.commit()


def get_challenges(user_id: str, db: Session):
    todos = db.query(Challenge).where(Challenge.user_id == user_id).all()

    return map(
        lambda todo: ChallengeDto(
            id=todo.id,
            title=todo.title,
            description=todo.description,
            completed=todo.completed,
        ),
        todos,
    )


def update_challenge(
    user_id: str, challenge_id: int, body: UpdateChallengeDto, db: Session
):
    challenge = db.query(Challenge).where(Challenge.id == challenge_id).first()

    if challenge is None:
        raise HTTPException(status_code=400, detail="챌린지를 찾을 수 없습니다.")

    if challenge.user_id is not user_id:
        raise HTTPException(status_code=403, detail="챌린지를 수정할 권한이 없습니다.")

    challenge.completed = body.completed
    challenge.completed_at = datetime.now() if body.completed else None

    db.commit()


def delete_challenge(challenge_id: int, user_id: str, db: Session):
    challenge = db.query(Challenge).where(Challenge.id == challenge_id).first()

    if challenge is None:
        raise HTTPException(status_code=400, detail="챌린지를 찾을 수 없습니다.")

    if challenge.user_id is not user_id:
        raise HTTPException(status_code=403, detail="챌린지를 삭제할 권한이 없습니다.")

    db.delete(challenge)
    db.commit()
