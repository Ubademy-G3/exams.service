from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional
'''
from enum import Enum

class QuestionTypeEnum(Enum):
    multiple_choice = 1
    written = 2
    media = 3
'''
class QuestionTemplate(BaseModel):
    id: UUID
    exam_id: UUID
    question: str
    type: str#QuestionTypeEnum
    options: Optional[dict]
    correct: Optional[int]

class QuestionTemplatePatch(BaseModel):
    question: Optional[str]
    type: Optional[str]
    options: Optional[dict]
    correct: Optional[int]

class QuestionTemplateSchema(BaseModel):
    exam_id: UUID
    question: str
    type: str
    options: Optional[dict]
    correct: Optional[int]