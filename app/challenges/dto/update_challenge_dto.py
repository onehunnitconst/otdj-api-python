from pydantic import BaseModel

class UpdateChallengeDto(BaseModel):
    completed: bool
