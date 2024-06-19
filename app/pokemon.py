from pydantic import BaseModel

class Pokemon(BaseModel):
    name: str
    type: str