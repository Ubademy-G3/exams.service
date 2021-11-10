from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional

class ExamSolution(BaseModel):
    id: UUID = uuid4()
    name: str
    course_id: UUID
    user_id: UUID
    graded: bool
    score: int
    aprobal_state: bool

class ExamSolutionSchema(BaseModel):
    name: str
    course_id: UUID
    user_id: UUID
    graded: bool
    score: int
    aprobal_state: bool