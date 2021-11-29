from fastapi.testclient import TestClient
from main import app
from unittest import TestCase, mock
from persistence.repositories.question_template_repository_postgres import QuestionTemplateRepositoryPostgres
from infrastructure.db.question_template_schema import QuestionTemplate, QuestionTypeEnum
import json
import os


apikey = os.getenv("API_KEY")

qtrp = QuestionTemplateRepositoryPostgres()


client = TestClient(app)


# Post
post_header = {"apikey": apikey, "exam_template_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

post_body = {
    "question": "What is 1 + 1?",
}

# Get
get_header = {"apikey": apikey, "exam_template_id": "5122b737-f815-4e15-a56d-abbff2fee900", "question_template_id": "2be97039-8c07-48ae-a18e-16d4779b977b"}

return_from_get = QuestionTemplate(
    id="2be97039-8c07-48ae-a18e-16d4779b977b",
    exam_id="5122b737-f815-4e15-a56d-abbff2fee900",
    question="What is 1 + 1?",
    question_type=QuestionTypeEnum.written,
    options=None,
    correct=None,
    value=1,
)

# Get all by exam template id
get_all_by_exam_id_header = {"apikey": apikey, "exam_template_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

return_from_get_all_by_exam_id = [
    QuestionTemplate(
        id="2be97039-8c07-48ae-a18e-16d4779b977b",
        exam_id="5122b737-f815-4e15-a56d-abbff2fee900",
        question="What is 1 + 1?",
        question_type=QuestionTypeEnum.written,
        options=None,
        correct=None,
        value=1,
    )
]

# Delete
delete_header = {"apikey": apikey, "exam_template_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

return_from_delete = None

# Update
update_header = {"apikey": apikey, "exam_template_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

update_body = {
    "question": "What is 1 * 1?",
    "value": 2,
}


class QuestionTemplateMock(TestCase):

    @mock.patch.object(QuestionTemplateRepositoryPostgres, "add_question_template")
    def test_create_question_template(self, mock_post):
        mock_post.return_value = None

        exam_template_id = "5122b737-f815-4e15-a56d-abbff2fee900"

        response = client.post(
            f"/exams/{exam_template_id}/questions/",
            data=json.dumps(post_body),
            headers=post_header
        )
        assert response.status_code == 201, response.text
        data = response.json()
        assert data["exam_id"] == exam_template_id
        assert data["question"] == "What is 1 + 1?"
        assert data["question_type"] == "written"
        assert data["options"] is None
        assert data["correct"] is None
        assert data["value"] == 1

    @mock.patch.object(QuestionTemplateRepositoryPostgres, "get_question_template")
    def test_get_question_template(self, mock_get):
        mock_get.return_value = return_from_get

        exam_template_id = "5122b737-f815-4e15-a56d-abbff2fee900"
        question_template_id = "2be97039-8c07-48ae-a18e-16d4779b977b"

        response = client.get(
            f"/exams/{exam_template_id}/questions/{question_template_id}",
            headers=get_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["id"] == question_template_id
        assert data["exam_id"] == exam_template_id
        assert data["question"] == "What is 1 + 1?"
        assert data["question_type"] == "written"
        assert data["options"] is None
        assert data["correct"] is None
        assert data["value"] == 1

    @mock.patch.object(QuestionTemplateRepositoryPostgres, "get_all_question_templates_by_exam_template_id")
    def test_get_all_by_exam_id(self, mock_get_all_by_exam_id):
        mock_get_all_by_exam_id.return_value = return_from_get_all_by_exam_id
        
        exam_template_id = "5122b737-f815-4e15-a56d-abbff2fee900"
        question_template_id = "2be97039-8c07-48ae-a18e-16d4779b977b"
        
        response = client.get(
            f"/exams/{exam_template_id}/questions/",
            headers=get_all_by_exam_id_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["exam_template_id"] == exam_template_id
        assert data["amount"] == 1
        assert data["question_templates"][0]["id"] == question_template_id
        assert data["question_templates"][0]["exam_id"] == exam_template_id
        assert data["question_templates"][0]["question"] == "What is 1 + 1?"
        assert data["question_templates"][0]["question_type"] == "written"
        assert data["question_templates"][0]["options"] is None
        assert data["question_templates"][0]["correct"] is None
        assert data["question_templates"][0]["value"] == 1

    @mock.patch.object(QuestionTemplateRepositoryPostgres, "delete_question_template")
    @mock.patch.object(QuestionTemplateRepositoryPostgres, "get_question_template")
    def test_delete_question_template(self, mock_get, mock_delete):
        mock_get.return_value = return_from_get
        mock_delete.return_value = return_from_delete

        exam_template_id = "5122b737-f815-4e15-a56d-abbff2fee900"
        question_template_id = "2be97039-8c07-48ae-a18e-16d4779b977b"

        response = client.delete(
            f"/exams/{exam_template_id}/questions/{question_template_id}",
            headers=delete_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["message"] == f"The question template {question_template_id} was deleted succesfully"

    @mock.patch.object(QuestionTemplateRepositoryPostgres, "update_question_template")
    @mock.patch.object(QuestionTemplateRepositoryPostgres, "get_question_template")
    def test_update_question_template(self, mock_get, mock_update):
        mock_get.return_value = return_from_get
        mock_update.return_value = None

        exam_template_id = "5122b737-f815-4e15-a56d-abbff2fee900"
        question_template_id = "2be97039-8c07-48ae-a18e-16d4779b977b"

        response = client.patch(
            f"/exams/{exam_template_id}/questions/{question_template_id}",
            data=json.dumps(update_body),
            headers=update_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["id"] == question_template_id
        assert data["exam_id"] == exam_template_id
        assert data["question"] == "What is 1 * 1?"
        assert data["question_type"] == "written"
        assert data["options"] is None
        assert data["correct"] is None
        assert data["value"] == 2
