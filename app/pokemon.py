from pydantic import BaseModel

class Pokemon(BaseModel):
    id: int
    name: str
    type: str
    evolution_level: int
    next_evolution_id: int
    previous_evolution_id: int