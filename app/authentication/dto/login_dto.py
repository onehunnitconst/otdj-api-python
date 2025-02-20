from pydantic import BaseModel;

class LoginDto(BaseModel):
    user_id: str
    password: str