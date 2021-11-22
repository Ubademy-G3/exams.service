from pydantic import BaseModel
from uuid import UUID
from typing import Optional, List
import enum


class QuestionTypeEnum(enum.Enum):
    multiple_choice = 1
    written = 2
    media = 3


class QuestionTemplatePostBody(BaseModel):
    question: str
    question_type: Optional[str]
    options: Optional[dict]
    correct: Optional[int]
    value: Optional[float]


class QuestionTemplateDB(BaseModel):
    id: UUID
    exam_id: UUID
    question: str
    question_type: str
    options: Optional[dict]
    correct: Optional[int]
    value: float


class QuestionTemplateList(BaseModel):
    amount: int
    exam_template_id: UUID
    question_templates: Optional[List[QuestionTemplateDB]]


class QuestionTemplatePatch(BaseModel):
    question: Optional[str]
    question_type: Optional[str]
    options: Optional[dict]
    correct: Optional[int]
    value: Optional[float]
