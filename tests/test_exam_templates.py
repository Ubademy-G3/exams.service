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


# Post
post_header = {"apikey": apikey}

post_body = {
    "course_id": "2f120281-12cd-413f-8e6a-2678b6b92406",
    "creator_id": "f1e8ea4b-3909-4f66-80ca-aad491049bdf",
    "name": "Test name for exam"
}

# Get
get_header = {"apikey": apikey, "exam_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

return_from_get = ExamTemplate(
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

# Get all by course id
get_all_by_course_id_header = {"apikey": apikey, "course_id": "2f120281-12cd-413f-8e6a-2678b6b92406"}

return_from_get_all_by_course_id = [
    ExamTemplate(
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
]

# Get all by creator id
get_all_by_creator_id_header = {"apikey": apikey, "creator_id": "f1e8ea4b-3909-4f66-80ca-aad491049bdf"}

return_from_get_all_by_creator_id = [
    ExamTemplate(
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
]


# Delete
delete_header = {"apikey": apikey, "exam_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

return_from_delete = None

# Update
update_header = {"apikey": apikey, "exam_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

update_body = {
    "name": "Test name for exam",
    "state": "active",
    "max_score": 10,
    "has_multiple_choice": True,
    "has_written": False,
    "has_media": False,
    "max_attempts": 1
}


class ExamTemplateMock(TestCase):

    @mock.patch.object(ExamTemplateRepositoryPostgres, "add_exam_template")
    def test_create_exam_template(self, mock_post):
        mock_post.return_value = None

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

    @mock.patch.object(ExamTemplateRepositoryPostgres, "get_exam_template")
    def test_get_exam_template(self, mock_get):
        mock_get.return_value = return_from_get
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

    @mock.patch.object(ExamTemplateRepositoryPostgres, "get_all_exam_templates_by_course_id")
    def test_get_all_exam_templates_by_course_id(self, mock_get_all_by_course_id):
        mock_get_all_by_course_id.return_value = return_from_get_all_by_course_id
        course_id = "2f120281-12cd-413f-8e6a-2678b6b92406"
        response = client.get(
            f"/exams/course/{course_id}",
            headers=get_all_by_course_id_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["course_id"] == course_id
        assert data["amount"] == 1
        assert data["exam_templates"][0]["id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["exam_templates"][0]["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["exam_templates"][0]["creator_id"] == "f1e8ea4b-3909-4f66-80ca-aad491049bdf"
        assert data["exam_templates"][0]["name"] == "Test name for exam"
        assert data["exam_templates"][0]["state"] == "draft"
        assert data["exam_templates"][0]["max_score"] == 10
        assert data["exam_templates"][0]["has_multiple_choice"] is False
        assert data["exam_templates"][0]["has_written"] is False
        assert data["exam_templates"][0]["has_media"] is False
        assert data["exam_templates"][0]["max_attempts"] == 1

    @mock.patch.object(ExamTemplateRepositoryPostgres, "get_all_exam_templates_by_creator_id")
    def test_get_all_exam_templates_by_creator_id(self, mock_get_all_by_creator_id):
        mock_get_all_by_creator_id.return_value = return_from_get_all_by_creator_id
        creator_id = "f1e8ea4b-3909-4f66-80ca-aad491049bdf"
        response = client.get(
            f"/exams/creator/{creator_id}",
            headers=get_all_by_creator_id_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["creator_id"] == creator_id
        assert data["amount"] == 1
        assert data["exam_templates"][0]["id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["exam_templates"][0]["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["exam_templates"][0]["creator_id"] == "f1e8ea4b-3909-4f66-80ca-aad491049bdf"
        assert data["exam_templates"][0]["name"] == "Test name for exam"
        assert data["exam_templates"][0]["state"] == "draft"
        assert data["exam_templates"][0]["max_score"] == 10
        assert data["exam_templates"][0]["has_multiple_choice"] is False
        assert data["exam_templates"][0]["has_written"] is False
        assert data["exam_templates"][0]["has_media"] is False
        assert data["exam_templates"][0]["max_attempts"] == 1

    @mock.patch.object(ExamTemplateRepositoryPostgres, "delete_exam_template")
    @mock.patch.object(ExamTemplateRepositoryPostgres, "get_exam_template")
    def test_delete_exam_template(self, mock_get, mock_delete):
        mock_get.return_value = return_from_get
        mock_delete.return_value = return_from_delete
        exam_id = "5122b737-f815-4e15-a56d-abbff2fee900"
        response = client.delete(
            f"/exams/{exam_id}",
            headers=delete_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["message"] == f"The exam template {exam_id} was deleted successfully"

    @mock.patch.object(ExamTemplateRepositoryPostgres, "update_exam_template")
    @mock.patch.object(ExamTemplateRepositoryPostgres, "get_exam_template")
    def test_update_exam_template(self, mock_get, mock_update):
        mock_get.return_value = return_from_get
        mock_update.return_value = None
        exam_id = "5122b737-f815-4e15-a56d-abbff2fee900"
        response = client.patch(
            f"/exams/{exam_id}",
            data=json.dumps(update_body),
            headers=update_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["id"] == exam_id
        assert data["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["creator_id"] == "f1e8ea4b-3909-4f66-80ca-aad491049bdf"
        assert data["name"] == "Test name for exam"
        assert data["state"] == "active"
        assert data["max_score"] == 10
        assert data["has_multiple_choice"] is True
        assert data["has_written"] is False
        assert data["has_media"] is False
        assert data["max_attempts"] == 1
