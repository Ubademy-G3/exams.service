from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List

"""
from enum import Enum

class QuestionTypeEnum(Enum):
    multiple_choice = 1
    written = 2
    media = 3
"""
"""
class QuestionTemplate(BaseModel):
    id: UUID
    exam_id: UUID
    question: str
    type: str#QuestionTypeEnum
    options: Optional[dict]
    correct: Optional[int]
"""


class QuestionTemplateSchema(BaseModel):
    question: str
    is_written: Optional[bool]
    is_media: Optional[bool]
    options: Optional[dict]
    correct: Optional[int]
    value: Optional[int]


class QuestionTemplateDB(QuestionTemplateSchema):
    id: UUID


class QuestionTemplateList(BaseModel):
    amount: int
    exam_template_id: UUID
    QuestionTemplates: List[QuestionTemplateDB]


class QuestionTemplatePatch(BaseModel):
    question: Optional[str]
    is_written: Optional[bool]
    is_media: Optional[bool]
    options: Optional[dict]
    correct: Optional[int]
    value: Optional[int]
