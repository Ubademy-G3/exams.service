from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional

class QuestionSolution(BaseModel):
    id: UUID
    exam_id: UUID
    question: str
    type: str
    options: Optional[list]
    correct: Optional[int]
    user_id: UUID
    answer: str

class QuestionSolutionPatch(BaseModel):
    question: Optional[str]
    type: Optional[str]
    options: Optional[list]
    correct: Optional[int]
    answer: Optional[str]

class QuestionSolutionSchema(BaseModel):
    exam_id: UUID
    question: str
    type: str
    options: Optional[list]
    correct: Optional[int]
    user_id: UUID
    answer: str