from fastapi.testclient import TestClient
from main import app
from unittest import TestCase, mock
from persistence.repositories.exam_template_repository_postgres import ExamTemplateRepositoryPostgres
from persistence.repositories.exam_solution_repository_postgres import ExamSolutionRepositoryPostgres
from infrastructure.db.exam_solution_schema import ExamSolution
from infrastructure.db.exam_template_schema import ExamTemplate, ExamStateEnum
import json
import os


apikey = os.getenv("API_KEY")

esrp = ExamSolutionRepositoryPostgres()


client = TestClient(app)


# Post
post_header = {"apikey": apikey, "exam_template_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

post_body = {
    "course_id": "2f120281-12cd-413f-8e6a-2678b6b92406",
    "user_id": "943368d4-cfa2-442c-a41e-14b6645b4472",
    "max_score": 10
}

return_from_get_template = ExamTemplate(
    id="5122b737-f815-4e15-a56d-abbff2fee900",
    course_id="2f120281-12cd-413f-8e6a-2678b6b92406",
    creator_id="f1e8ea4b-3909-4f66-80ca-aad491049bdf",
    name="Test name for exam",
    state=ExamStateEnum.active,
    max_score=10,
    approval_score=10,
    has_multiple_choice=False,
    has_written=True,
    has_media=False,
    max_attempts=1,
)

# Get
get_header = {
    "apikey": apikey,
    "exam_template_id": "5122b737-f815-4e15-a56d-abbff2fee900",
    "exam_solution_id": "fe7c9444-3354-4ec4-b9f7-330638d752aa"
}

return_from_get = ExamSolution(
    id="fe7c9444-3354-4ec4-b9f7-330638d752aa",
    course_id="2f120281-12cd-413f-8e6a-2678b6b92406",
    user_id="943368d4-cfa2-442c-a41e-14b6645b4472",
    exam_template_id="5122b737-f815-4e15-a56d-abbff2fee900",
    corrector_id=None,
    graded=False,
    score=0,
    max_score=10,
    approval_state=False,
)

# Get all by exam template id
get_all_by_exam_template_id_header = {"apikey": apikey, "exam_template_id": "5122b737-f815-4e15-a56d-abbff2fee900"}

return_from_get_all_by_exam_template_id = [
    ExamSolution(
        id="fe7c9444-3354-4ec4-b9f7-330638d752aa",
        course_id="2f120281-12cd-413f-8e6a-2678b6b92406",
        user_id="943368d4-cfa2-442c-a41e-14b6645b4472",
        exam_template_id="5122b737-f815-4e15-a56d-abbff2fee900",
        corrector_id=None,
        graded=False,
        score=0,
        max_score=10,
        approval_state=False,
    )
]

# Get all by user id
get_all_by_user_id_header = {"apikey": apikey, "user_id": "f1e8ea4b-3909-4f66-80ca-aad491049bdf"}

return_from_get_all_by_user_id = [
    ExamSolution(
        id="fe7c9444-3354-4ec4-b9f7-330638d752aa",
        course_id="2f120281-12cd-413f-8e6a-2678b6b92406",
        user_id="943368d4-cfa2-442c-a41e-14b6645b4472",
        exam_template_id="5122b737-f815-4e15-a56d-abbff2fee900",
        corrector_id=None,
        graded=False,
        score=0,
        max_score=10,
        approval_state=False,
    )
]

# Get all by corrector id
get_all_by_corrector_id_header = {"apikey": apikey, "corrector_id": "2f120281-12cd-413f-8e6a-2678b6b92406"}

return_from_get_all_by_corrector_id = [
    ExamSolution(
        id="fe7c9444-3354-4ec4-b9f7-330638d752aa",
        course_id="2f120281-12cd-413f-8e6a-2678b6b92406",
        user_id="943368d4-cfa2-442c-a41e-14b6645b4472",
        exam_template_id="5122b737-f815-4e15-a56d-abbff2fee900",
        corrector_id="5384d830-c14a-4e1a-9215-9525307b24a8",
        graded=True,
        score=10,
        max_score=10,
        approval_state=True,
    )
]

# Get all by course id
get_all_by_course_id_header = {"apikey": apikey, "course_id": "2f120281-12cd-413f-8e6a-2678b6b92406"}

return_from_get_all_by_course_id = [
    ExamSolution(
        id="fe7c9444-3354-4ec4-b9f7-330638d752aa",
        course_id="2f120281-12cd-413f-8e6a-2678b6b92406",
        user_id="943368d4-cfa2-442c-a41e-14b6645b4472",
        exam_template_id="5122b737-f815-4e15-a56d-abbff2fee900",
        corrector_id=None,
        graded=False,
        score=0,
        max_score=10,
        approval_state=False,
    )
]


# Delete
delete_header = {
    "apikey": apikey,
    "exam_template_id": "5122b737-f815-4e15-a56d-abbff2fee900",
    "exam_solution_id": "fe7c9444-3354-4ec4-b9f7-330638d752aa"
}

return_from_delete = None

# Update
update_header = {
    "apikey": apikey,
    "exam_template_id": "5122b737-f815-4e15-a56d-abbff2fee900",
    "exam_solution_id": "fe7c9444-3354-4ec4-b9f7-330638d752aa"
}

update_body = {
    "corrector_id": "5384d830-c14a-4e1a-9215-9525307b24a8",
    "graded": True,
    "score": 10,
    "approval_state": True,
}

second_update_body = {
    "corrector_id": "5384d830-c14a-4e1a-9215-9525307b24a8",
    "score": 4,
}


class ExamSolutionMock(TestCase):

    @mock.patch.object(ExamSolutionRepositoryPostgres, "add_exam_solution")
    @mock.patch.object(ExamSolutionRepositoryPostgres, "get_all_exam_solutions_by_user_id_and_exam_template_id")
    @mock.patch.object(ExamTemplateRepositoryPostgres, "get_exam_template")
    def test_create_exam_solution(self, mock_get, mock_get_all, mock_post):
        mock_get.return_value = return_from_get_template
        mock_get_all.return_value = []
        mock_post.return_value = None

        exam_template_id = "5122b737-f815-4e15-a56d-abbff2fee900"

        response = client.post(
            f"/exams/{exam_template_id}/solutions/",
            data=json.dumps(post_body),
            headers=post_header
        )
        assert response.status_code == 201, response.text
        data = response.json()
        assert data["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["user_id"] == "943368d4-cfa2-442c-a41e-14b6645b4472"
        assert data["exam_template_id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["corrector_id"] is None
        assert data["graded"] is False
        assert data["score"] == 0
        assert data["max_score"] == 10
        assert data["approval_state"] is False

    @mock.patch.object(ExamSolutionRepositoryPostgres, "get_exam_solution")
    def test_get_exam_solution(self, mock_get):
        mock_get.return_value = return_from_get

        exam_template_id = "5122b737-f815-4e15-a56d-abbff2fee900"
        exam_solution_id = "fe7c9444-3354-4ec4-b9f7-330638d752aa"

        response = client.get(
            f"/exams/{exam_template_id}/solutions/{exam_solution_id}/",
            headers=get_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["id"] == exam_solution_id
        assert data["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["user_id"] == "943368d4-cfa2-442c-a41e-14b6645b4472"
        assert data["exam_template_id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["corrector_id"] is None
        assert data["graded"] is False
        assert data["score"] == 0
        assert data["max_score"] == 10
        assert data["approval_state"] is False

    @mock.patch.object(ExamSolutionRepositoryPostgres, "get_all_exam_solutions_by_exam_template_id")
    def test_get_all_exam_solutions_by_exam_template_id(self, mock_get_all_by_exam_template_id):
        mock_get_all_by_exam_template_id.return_value = return_from_get_all_by_exam_template_id

        exam_template_id = "5122b737-f815-4e15-a56d-abbff2fee900"

        response = client.get(
            f"/exams/{exam_template_id}/solutions/",
            headers=get_all_by_exam_template_id_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["exam_template_id"] == exam_template_id
        assert data["amount"] == 1
        assert data["exam_solutions"][0]["id"] == "fe7c9444-3354-4ec4-b9f7-330638d752aa"
        assert data["exam_solutions"][0]["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["exam_solutions"][0]["user_id"] == "943368d4-cfa2-442c-a41e-14b6645b4472"
        assert data["exam_solutions"][0]["exam_template_id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["exam_solutions"][0]["corrector_id"] is None
        assert data["exam_solutions"][0]["graded"] is False
        assert data["exam_solutions"][0]["score"] == 0
        assert data["exam_solutions"][0]["max_score"] == 10
        assert data["exam_solutions"][0]["approval_state"] is False

    @mock.patch.object(ExamSolutionRepositoryPostgres, "get_all_exam_solutions_by_user_id")
    def test_get_all_exam_solutions_by_user_id(self, mock_get_all_by_user_id):
        mock_get_all_by_user_id.return_value = return_from_get_all_by_user_id

        user_id = "943368d4-cfa2-442c-a41e-14b6645b4472"

        response = client.get(
            f"/exams/solutions/user/{user_id}/",
            headers=get_all_by_user_id_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["user_id"] == user_id
        assert data["amount"] == 1
        assert data["exam_solutions"][0]["id"] == "fe7c9444-3354-4ec4-b9f7-330638d752aa"
        assert data["exam_solutions"][0]["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["exam_solutions"][0]["user_id"] == "943368d4-cfa2-442c-a41e-14b6645b4472"
        assert data["exam_solutions"][0]["exam_template_id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["exam_solutions"][0]["corrector_id"] is None
        assert data["exam_solutions"][0]["graded"] is False
        assert data["exam_solutions"][0]["score"] == 0
        assert data["exam_solutions"][0]["max_score"] == 10
        assert data["exam_solutions"][0]["approval_state"] is False

    @mock.patch.object(ExamSolutionRepositoryPostgres, "get_all_exam_solutions_by_course_id")
    def test_get_all_exam_solutions_by_course_id(self, mock_get_all_by_course_id):
        mock_get_all_by_course_id.return_value = return_from_get_all_by_course_id

        course_id = "2f120281-12cd-413f-8e6a-2678b6b92406"

        response = client.get(
            f"/exams/solutions/course/{course_id}/",
            headers=get_all_by_course_id_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["course_id"] == course_id
        assert data["amount"] == 1
        assert data["exam_solutions"][0]["id"] == "fe7c9444-3354-4ec4-b9f7-330638d752aa"
        assert data["exam_solutions"][0]["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["exam_solutions"][0]["user_id"] == "943368d4-cfa2-442c-a41e-14b6645b4472"
        assert data["exam_solutions"][0]["exam_template_id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["exam_solutions"][0]["corrector_id"] is None
        assert data["exam_solutions"][0]["graded"] is False
        assert data["exam_solutions"][0]["score"] == 0
        assert data["exam_solutions"][0]["max_score"] == 10
        assert data["exam_solutions"][0]["approval_state"] is False

    @mock.patch.object(ExamSolutionRepositoryPostgres, "get_all_exam_solutions_by_corrector_id")
    def test_get_all_exam_solutions_by_corrector_id(self, mock_get_all_by_corrector_id):
        mock_get_all_by_corrector_id.return_value = return_from_get_all_by_corrector_id

        corrector_id = "2f120281-12cd-413f-8e6a-2678b6b92406"

        response = client.get(
            f"/exams/solutions/corrector/{corrector_id}/",
            headers=get_all_by_corrector_id_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["corrector_id"] == corrector_id
        assert data["amount"] == 1
        assert data["exam_solutions"][0]["id"] == "fe7c9444-3354-4ec4-b9f7-330638d752aa"
        assert data["exam_solutions"][0]["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["exam_solutions"][0]["user_id"] == "943368d4-cfa2-442c-a41e-14b6645b4472"
        assert data["exam_solutions"][0]["exam_template_id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["exam_solutions"][0]["corrector_id"] == "5384d830-c14a-4e1a-9215-9525307b24a8"
        assert data["exam_solutions"][0]["graded"] is True
        assert data["exam_solutions"][0]["score"] == 10
        assert data["exam_solutions"][0]["max_score"] == 10
        assert data["exam_solutions"][0]["approval_state"] is True

    @mock.patch.object(ExamSolutionRepositoryPostgres, "delete_exam_solution")
    @mock.patch.object(ExamSolutionRepositoryPostgres, "get_exam_solution")
    def test_delete_exam_solution(self, mock_get, mock_delete):
        mock_get.return_value = return_from_get
        mock_delete.return_value = return_from_delete

        exam_template_id = "5122b737-f815-4e15-a56d-abbff2fee900"
        exam_solution_id = "fe7c9444-3354-4ec4-b9f7-330638d752aa"

        response = client.delete(
            f"/exams/{exam_template_id}/solutions/{exam_solution_id}/",
            headers=delete_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["message"] == f"The exam solution {exam_solution_id} was deleted successfully"

    @mock.patch.object(ExamSolutionRepositoryPostgres, "update_exam_solution")
    @mock.patch.object(ExamSolutionRepositoryPostgres, "get_exam_solution")
    def test_update_exam_solution(self, mock_get, mock_update):
        mock_get.return_value = return_from_get
        mock_update.return_value = None

        exam_template_id = "5122b737-f815-4e15-a56d-abbff2fee900"
        exam_solution_id = "fe7c9444-3354-4ec4-b9f7-330638d752aa"

        response = client.patch(
            f"/exams/{exam_template_id}/solutions/{exam_solution_id}/",
            data=json.dumps(update_body),
            headers=update_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["id"] == exam_solution_id
        assert data["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["user_id"] == "943368d4-cfa2-442c-a41e-14b6645b4472"
        assert data["exam_template_id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["corrector_id"] == "5384d830-c14a-4e1a-9215-9525307b24a8"
        assert data["graded"] is True
        assert data["score"] == 10
        assert data["max_score"] == 10
        assert data["approval_state"] is True

    @mock.patch.object(ExamSolutionRepositoryPostgres, "update_exam_solution")
    @mock.patch.object(ExamSolutionRepositoryPostgres, "get_exam_solution")
    def test_partial_update_exam_solution(self, mock_get, mock_update):
        mock_get.return_value = return_from_get
        mock_update.return_value = None

        exam_template_id = "5122b737-f815-4e15-a56d-abbff2fee900"
        exam_solution_id = "fe7c9444-3354-4ec4-b9f7-330638d752aa"

        response = client.patch(
            f"/exams/{exam_template_id}/solutions/{exam_solution_id}/",
            data=json.dumps(second_update_body),
            headers=update_header
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["id"] == exam_solution_id
        assert data["course_id"] == "2f120281-12cd-413f-8e6a-2678b6b92406"
        assert data["user_id"] == "943368d4-cfa2-442c-a41e-14b6645b4472"
        assert data["exam_template_id"] == "5122b737-f815-4e15-a56d-abbff2fee900"
        assert data["corrector_id"] == "5384d830-c14a-4e1a-9215-9525307b24a8"
        assert data["graded"] is False
        assert data["score"] == 4
        assert data["max_score"] == 10
        assert data["approval_state"] is False
