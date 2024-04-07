import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.core.db import get_db_session
from src.models import Teacher

client = TestClient(app)


def test_get_teachers():
    response = client.get("/teachers/")
    assert response.status_code == 200
    teachers = response.json()
    assert isinstance(teachers, list)
    for teacher in teachers:
        assert "name" in teacher
        assert "surname" in teacher
        assert "patronymic" in teacher


def test_put_teacher_single():
    teacher_data = {"name": "John", "surname": "Doe", "patronymic": "Smith"}
    response = client.put("/teachers/", json=teacher_data)
    assert response.status_code == 201


def test_put_teacher_multiple():
    teachers_data = [
        {"name": "John", "surname": "Doe", "patronymic": "Smith"},
        {"name": "Jane", "surname": "Doe", "patronymic": "Smith"},
    ]
    response = client.put("/teachers/", json=teachers_data)
    assert response.status_code == 201


def test_put_teacher_invalid_payload():
    invalid_teacher_data = {"invalid_field": "Invalid Value"}
    response = client.put("/teachers/", json=invalid_teacher_data)
    assert response.status_code == 422


# Ensure to clean up any test data inserted during testing
def teardown():
    pass


@pytest.fixture(autouse=True)
def setup_teardown():
    get_db_session()
    yield
    teardown()
