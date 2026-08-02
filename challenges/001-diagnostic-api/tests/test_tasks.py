from fastapi.testclient import TestClient

from diagnostic_api.main import create_app


def test_task_is_created_and_listed() -> None:
    client = TestClient(create_app())

    response = client.post(
        "/tasks",
        json={"title": "Write release notes", "description": "First draft", "priority": 2},
    )

    assert response.status_code == 201
    created = response.json()
    assert created["id"] == 1
    assert created["title"] == "Write release notes"
    assert created["description"] == "First draft"
    assert created["priority"] == 2
    assert created["status"] == "todo"

    listed = client.get("/tasks")

    assert listed.status_code == 200
    assert listed.json() == [created]


def test_tasks_can_be_filtered_by_initial_status() -> None:
    client = TestClient(create_app())
    client.post("/tasks", json={"title": "Check deployment"})

    response = client.get("/tasks", params={"status": "todo"})

    assert response.status_code == 200
    assert response.json()[0]["title"] == "Check deployment"
