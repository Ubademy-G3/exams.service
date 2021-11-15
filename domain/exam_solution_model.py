from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional

class ExamSolution(BaseModel):
    id: UUID
    name: str
    course_id: UUID
    user_id: UUID
    graded: bool = False
    score: int = 0
    aprobal_state: bool = False


class ExamSolutionPatch(BaseModel):
    graded: Optional[bool]
    score: Optional[int]
    aprobal_state: Optional[bool]

class ExamSolutionSchema(BaseModel):
    name: str
    course_id: UUID
    user_id: UUID