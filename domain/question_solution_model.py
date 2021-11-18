from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional, List
'''
class QuestionSolution(BaseModel):
    id: UUID
    exam_id: UUID
    question: str
    type: str
    options: Optional[list]
    correct: Optional[int]
    user_id: UUID
    answer: str
'''

class QuestionSolutionSchema(BaseModel):
    exam_solution_id: UUID
    question_template_id: UUID
    answer: str

class QuestionSolutionDB(QuestionSolutionSchema):
    id: UUID

class QuestionSolutionList(BaseModel):
    amount: int
    exam_solution_id: UUID
    QuestionSolutions: List[QuestionSolutionDB]

class QuestionSolutionPatch(BaseModel):
    answer: Optional[str]
    score: Optional[int]