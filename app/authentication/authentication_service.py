from fastapi import HTTPException
from fastapi.logger import logger
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from sqlalchemy.orm import Session
from authentication.dto.login_dto import LoginDto
from authentication.dto.register_dto import RegisterDto
from authentication.dto.login_response_dto import LoginResponseDto
from db.models import User
import jwt

jwt_secret = 'jwt_test'

def login(db: Session, ph: PasswordHasher, body: LoginDto):
    user = db.query(User).where(User.user_id == body.user_id).first()

    if user == None:
        raise HTTPException(status_code=404, detail="가입된 사용자가 아닙니다.")

    try:
        ph.verify(user.password, body.password)
    except VerifyMismatchError:
        raise HTTPException(status_code=401, detail="비밀번호가 일치하지 않습니다.")
    
    token = jwt.encode({ "user_id": user.id }, jwt_secret)
    
    return LoginResponseDto(token=token)

def register(db: Session, ph: PasswordHasher, body: RegisterDto):
    user = db.query(User).where(User.user_id == body.user_id).first()

    if user != None:
        raise HTTPException(status_code=400, detail="이미 가입된 아이디입니다.")

    hashed_password = ph.hash(body.password)

    new_user = User(
        user_id=body.user_id,
        password=hashed_password,
        nickname=body.nickname,
    )

    db.add(new_user)
    db.commit()