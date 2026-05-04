# schemas.py
from pydantic import BaseModel

class MatchSchema(BaseModel):
    id: int
    team_a: str
    team_b: str
    status: str
