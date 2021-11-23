from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List


class ExamSolutionPostBody(BaseModel):
    course_id: UUID
    user_id: UUID
    corrector_id: UUID
    max_score: float


class ExamSolutionDB(BaseModel):
    id: UUID
    course_id: UUID
    user_id: UUID
    exam_template_id: UUID
    corrector_id: UUID
    graded: bool
    score: Optional[float]
    max_score: float
    approval_state: Optional[bool]


class ExamSolutionList(BaseModel):
    exam_template_id: UUID
    amount: int
    amount_graded: int
    average_score: Optional[float]
    approval_rate: Optional[float]
    exam_solutions: Optional[List[ExamSolutionDB]]


class UserExamSolutionList(BaseModel):
    user_id: UUID
    amount: int
    amount_graded: int
    average_score: Optional[float]
    approval_rate: Optional[float]
    exam_solutions: Optional[List[ExamSolutionDB]]


class CourseExamSolutionList(BaseModel):
    course_id: UUID
    amount: int
    amount_graded: int
    average_score: Optional[float]
    approval_rate: Optional[float]
    exam_solutions: Optional[List[ExamSolutionDB]]


class CorrectorExamSolutionList(BaseModel):
    corrector_id: UUID
    amount: int
    amount_graded: int
    approval_rate: Optional[float]
    exam_solutions: Optional[List[ExamSolutionDB]]


class ExamSolutionPatch(BaseModel):
    corrector_id: UUID
    graded: bool
    score: float
    approval_state: bool
