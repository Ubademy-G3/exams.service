from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional

class QuestionTemplate(BaseModel):
    id: UUID = uuid4()
    exam_id: UUID
    question: str
    type: str
    options: Optional[list]
    correct: Optional[int]

class QuestionTemplatePatch(BaseModel):
    question: Optional[str]
    type: Optional[str]
    options: Optional[list]
    correct: Optional[int]

class QuestionTemplateSchema(BaseModel):
    exam_id: UUID
    question: str
    type: str
    options: Optional[list]
    correct: Optional[int]