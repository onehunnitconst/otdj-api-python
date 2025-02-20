from fastapi import Depends, HTTPException
from fastapi.logger import logger
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt import InvalidTokenError, ExpiredSignatureError

from settings import Settings, get_settings

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_user_id(
    token: str = Depends(oauth2_scheme), settings: Settings = Depends(get_settings)
):
    try:
        payload = jwt.decode(
            token,
            key=settings.jwt_secret,
            algorithms=[settings.jwt_algorithm],
        )
        user_id = payload.get("user_id")
        if user_id is None:
            raise HTTPException(status_code=401, detail="로그인 되어있지 않습니다.")
        return user_id
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="토큰이 만료되었습니다.")
    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="유효하지 않은 토큰입니다.")
