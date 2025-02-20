from pydantic import BaseModel;

class RegisterDto(BaseModel):
    user_id: str
    password: str
    nickname: str