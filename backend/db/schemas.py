from pydantic import BaseModel

class User(BaseModel):
    id: int
    email: str
    is_active: bool = True

class Newsletter(BaseModel):
    