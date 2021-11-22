from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List


class ExamSolutionPostBody(BaseModel):
    course_id: UUID
    user_id: UUID


class ExamSolutionDB(BaseModel):
    id: UUID
    course_id: UUID
    user_id: UUID
    exam_template_id: UUID
    graded: bool
    score: Optional[float]
    approval_state: Optional[bool]
    corrector_id: Optional[UUID]


class ExamSolutionList(BaseModel):
    amount: int
    exam_template_id: UUID
    average_score: Optional[float]
    exam_solutions: Optional[List[ExamSolutionDB]]


class UserExamSolutionList(BaseModel):
    amount: int
    user_id: UUID
    average_score: Optional[float]
    exam_solutions: Optional[List[ExamSolutionDB]]


class CourseExamSolutionList(BaseModel):
    amount: int
    course_id: UUID
    average_score: Optional[float]
    exam_solutions: Optional[List[ExamSolutionDB]]


class CorrectorExamSolutionList(BaseModel):
    amount: int
    corrector_id: UUID
    exam_solutions: Optional[List[ExamSolutionDB]]


class ExamSolutionPatch(BaseModel):
    graded: Optional[bool]
    score: Optional[float]
    approval_state: Optional[bool]
    corrector_id: UUID
