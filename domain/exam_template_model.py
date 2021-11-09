from pydantic import BaseModel
from uuid import uuid4, UUID
from typing import Optional

class ExamTemplate(BaseModel):
    id: UUID = uuid4()
    name: str
    course_id: UUID
    questions: list

class ExamTemplatePatch(BaseModel):
    name: Optional[str]
    course_id: Optional[UUID]
    questions: Optional[list]

class ExamTemplateSchema(BaseModel):
    name: str
    course_id: UUID
    questions: list