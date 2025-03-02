from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class ChallengeDto(BaseModel):
    id: int
    song_title: str
    song_artist: str
    song_cover: str
    chart_type: str
    chart_difficulty: str
    chart_level: str
    chart_constant: float
    challenge_type: str
    challenge_goal: str
    completed: bool
    completed_at: Optional[datetime]
