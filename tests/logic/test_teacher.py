import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.core.db import get_db_session

client = TestClient(app)


def test_get_teachers():
    response = client.get("/teachers/")
    assert response.status_code == 200


def test_put_teacher():
    teacher_data = {"name": "Test Teacher", "subject": "Test Subject"}
    response = client.put("/teachers/", json=teacher_data)
    assert response.status_code == 422


def test_put_teacher_invalid_payload():
    invalid_teacher_data = {"invalid_field": "Invalid Value"}
    response = client.put("/teachers/", json=invalid_teacher_data)
    assert response.status_code == 422


def teardown():
    pass


@pytest.fixture(autouse=True)
def setup_teardown():
    get_db_session()
    yield
    teardown()
