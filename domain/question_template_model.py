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


class QuestionTemplatePostBody(BaseModel):
    question: str
    is_written: Optional[bool]
    is_media: Optional[bool]
    options: Optional[dict]
    correct: Optional[int]
    value: Optional[int]


class QuestionTemplateDB(BaseModel):
    id: UUID
    exam_id: UUID
    question: str
    is_written: bool
    is_media: bool
    options: Optional[dict]
    correct: Optional[int]
    value: int


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
