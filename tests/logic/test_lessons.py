import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.core.db import get_db_session
from src.models import Teacher, Lesson, Place

client = TestClient(app)


def test_get_timetable():
    response = client.get("/lessons/timetable")
    assert response.status_code == 200
    timetable_items = response.json()
    assert isinstance(timetable_items, list)
    assert all(isinstance(item, (Teacher, Lesson, Place)) for item in timetable_items)


def test_put_lesson():
    lesson_data = {"attribute1": "value1", "attribute2": "value2"}  # Replace with actual data
    response = client.put("/lessons/", json=lesson_data)
    assert response.status_code == 201


def test_put_lesson_invalid_payload():
    invalid_lesson_data = {"invalid_field": "Invalid Value"}
    response = client.put("/lessons/", json=invalid_lesson_data)
    assert response.status_code == 422


def teardown():
    pass


@pytest.fixture(autouse=True)
def setup_teardown():
    get_db_session()
    yield
    teardown()
