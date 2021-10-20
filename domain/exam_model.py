from pydantic import BaseModel


class Exam(BaseModel):
    id: int
    name: str
