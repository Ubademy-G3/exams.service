from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List

"""
class ExamSolution(BaseModel):
    id: UUID
    name: str
    course_id: UUID
    user_id: UUID
    graded: bool = False
    score: int = 0
    aprobal_state: bool = False
"""


class ExamSolutionPostBody(BaseModel):
    course_id: UUID
    user_id: UUID


class ExamSolutionDB(BaseModel):
    id: UUID
    course_id: UUID
    user_id: UUID
    exam_template_id: UUID
    graded: bool
    score: int
    aprobal_state: bool


class UserExamSolutionList(BaseModel):
    amount: int
    user_id: UUID
    ExamSolutions: Optional[List[ExamSolutionDB]]


class ExamSolutionList(BaseModel):
    amount: int
    exam_template_id: UUID
    ExamSolutions: Optional[List[ExamSolutionDB]]


class ExamSolutionPatch(BaseModel):
    graded: Optional[bool]
    score: Optional[int]
    aprobal_state: Optional[bool]
