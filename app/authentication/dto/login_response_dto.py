from pydantic import BaseModel;

class LoginResponseDto(BaseModel):
    token: str