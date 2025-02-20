from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from argon2 import PasswordHasher

from settings import Settings, get_settings
from modules.password_hash import get_password_hasher
from db.database import get_session
from authentication.dto.login_dto import LoginDto
from authentication.dto.register_dto import RegisterDto
from authentication import authentication_service

router = APIRouter(prefix="/authentication")


@router.post("/login")
def login(
    body: LoginDto,
    db: Session = Depends(get_session),
    ph: PasswordHasher = Depends(get_password_hasher),
    settings: Settings = Depends(get_settings)
):
    return authentication_service.login(
        body=body,
        db=db,
        ph=ph,
        settings=settings
    )


@router.post("/register")
def register(
    body: RegisterDto,
    db: Session = Depends(get_session),
    ph: PasswordHasher = Depends(get_password_hasher),
):
    return authentication_service.register(
        body=body,
        db=db,
        ph=ph,
    )
