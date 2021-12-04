from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List


class QuestionSolutionPostBody(BaseModel):
    question_template_id: UUID
    answer: str


class QuestionSolutionDB(BaseModel):
    id: UUID
    exam_solution_id: UUID
    question_template_id: UUID
    answer: Optional[str]
    score: Optional[float]


class QuestionSolutionList(BaseModel):
    exam_solution_id: UUID
    amount: int
    total_score: float
    question_solutions: Optional[List[QuestionSolutionDB]]


class UserQuestionSolutionList(BaseModel):
    exam_solution_id: UUID
    amount: int
    average: Optional[float]
    question_solutions: Optional[List[QuestionSolutionDB]]


class QuestionSolutionPatch(BaseModel):
    answer: Optional[str]
    score: Optional[float]
