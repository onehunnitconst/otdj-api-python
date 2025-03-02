from pydantic import BaseModel

class CreateChallengeDto(BaseModel):
    song_id: int
    chart_id: int
    challenge_type: str
    challenge_goal: str
