import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.core.db import get_db_session
from src.models import Lesson

client = TestClient(app)


def test_get_timetable():
    response = client.get("/lessons/timetable")
    assert response.status_code == 200
    timetable_items = response.json()
    assert isinstance(timetable_items, list)
    for item in timetable_items:
        assert "id" in item
        assert "subject" in item
        assert "type" in item
        assert "week_day" in item
        assert "start" in item
        assert "cabinet" in item
        assert "pavilion" in item
        assert "teacher" in item


def test_put_lesson_single():
    lesson_data = {
        "subject": "Math",
        "type": "Lecture",
        "week_day": "Monday",
        "start": "10:00:00",
        "teacher_id": 1,
        "place_id": 1
    }
    response = client.put("/lessons/", json=lesson_data)
    assert response.status_code == 201


def test_put_lesson_multiple():
    lessons_data = [
        {
            "subject": "Math",
            "type": "Lecture",
            "week_day": "Monday",
            "start": "10:00:00",
            "teacher_id": 1,
            "place_id": 1
        },
        {
            "subject": "Physics",
            "type": "Practice",
            "week_day": "Tuesday",
            "start": "12:00:00",
            "teacher_id": 2,
            "place_id": 2
        }
    ]
    response = client.put("/lessons/", json=lessons_data)
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
