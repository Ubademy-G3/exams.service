from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional
from typing import List

from domain.question_template_model import QuestionTemplateSchema

class ExamTemplate(BaseModel):
    name: str
    course_id: UUID
    active: bool = True

class ExamTemplatePatch(BaseModel):
    name: Optional[str]
    active: Optional[bool]

class ExamTemplateSchema(BaseModel):
    name: str
    course_id: UUID