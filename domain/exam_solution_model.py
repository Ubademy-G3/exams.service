from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional

class ExamSolution(BaseModel):
    id: UUID
    name: str
    course_id: UUID
    user_id: UUID
    answers: list
    graded: bool
    score: int
    aprobal_state: bool

'''
class ExamSolutionPatch(BaseModel):
    name: Optional[str]
    course_id: Optional[UUID]
    questions: Optional[list]
'''