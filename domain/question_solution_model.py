from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List

"""
class QuestionSolution(BaseModel):
    id: UUID
    exam_id: UUID
    question: str
    type: str
    options: Optional[list]
    correct: Optional[int]
    user_id: UUID
    answer: str
"""


class QuestionSolutionPostBody(BaseModel):
    question_template_id: UUID
    answer: str


class QuestionSolutionDB(BaseModel):
    id: UUID
    exam_solution_id: UUID
    question_template_id: UUID
    answer: str
    score: float


class QuestionSolutionList(BaseModel):
    amount: int
    exam_solution_id: UUID
    total_score: float
    question_solutions: Optional[List[QuestionSolutionDB]]


class UserQuestionSolutionList(BaseModel):
    amount: int
    exam_solution_id: UUID
    average: Optional[float]
    question_solutions: Optional[List[QuestionSolutionDB]]


class QuestionSolutionPatch(BaseModel):
    answer: Optional[str]
    score: Optional[float]
