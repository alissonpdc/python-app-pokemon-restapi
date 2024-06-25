from pydantic import BaseModel
from typing import Optional

class Pokemon(BaseModel):
    id: int
    name: str
    type: str
    evolution_level: int
    next_evolution_id: Optional[int]
    previous_evolution_id: Optional[int]