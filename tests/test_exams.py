from fastapi.testclient import TestClient
from main import app
from unittest import TestCase, mock
from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from infrastructure.db.exam_template_schema import ExamTemplate, ExamStateEnum
import json
import os


apikey = os.getenv("API_KEY")

etrp = ExamTemplateRepositoryPostgres()


client = TestClient(app)


post_header = {"apikey": apikey}

post_body = {
    "course_id": "2f120281-12cd-413f-8e6a-2678b6b92406",
    "creator_id": "f1e8ea4b-3909-4f66-80ca-aad491049bdf",
    "name": "Test name for exam"
}


class CreateExamTemplateMock(TestCase):

    @mock.patch.object(ExamTemplateRepositoryPostgres, "add_exam_template")
    def test_create_exam_template(self, mock_method):
        mock_method.return_value = None

        response = client.post(
            "/exams/",
            data=json.dumps(post_body),
            headers=post_header
        )
        assert response.status_code == 201, response.text
        data = response.json()
        assert data["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["creator_id"] == "f1e8ea4b-3909-4f66-80ca-aad491049bdf"
        assert data["name"] == "Test name for exam"
        assert data["state"] == "draft"


get_header = {"apikey": apikey, "exam_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

get_body = None

result_from_get = ExamTemplate(
    id="5122b737-f815-4e15-a56d-abbff2fee900",
    course_id="2f120281-12cd-413f-8e6a-2678b6b92406",
    creator_id="f1e8ea4b-3909-4f66-80ca-aad491049bdf",
    name="Test name for exam",
    state=ExamStateEnum.draft,
    max_score=10,
    has_multiple_choice=False,
    has_written=False,
    has_media=False,
    max_attempts=1,
)


class GetExamTemplateMock(TestCase):

    @mock.patch.object(ExamTemplateRepositoryPostgres, "get_exam_template")
    def test_create_exam_template(self, mock_method):
        mock_method.return_value = result_from_get
        exam_id = "5122b737-f815-4e15-a56d-abbff2fee900"
        response = client.get(
            f"/exams/{exam_id}",
            headers=get_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["id"] == exam_id
        assert data["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["creator_id"] == "f1e8ea4b-3909-4f66-80ca-aad491049bdf"
        assert data["name"] == "Test name for exam"
        assert data["state"] == "draft"
        assert data["max_score"] == 10
        assert data["has_multiple_choice"] is False
        assert data["has_written"] is False
        assert data["has_media"] is False
        assert data["max_attempts"] == 1
