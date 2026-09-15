import pytest
from app.app import  app

@pytest.fixture
def client():
	app.config["TESTING"] = True

	with app.test_client() as client:
		yield client

def test_health(client):
	response = client.get("/health")

	assert response.status_code == 200
	assert response.get_json() == {"status": "healthy"}

def test_create_task(client):
	response = client.post(
		"/tasks",
		json={"title": "Learn Jenkins"}
	)

	assert response.status_code == 201

	data = response.get_json()

	assert data["title"] == "Learn Jenkins"
	assert data["completed"] is False

def test_get_tasks(client):
        response = client.get("/tasks")

        assert response.status_code == 200

        data = response.get_json()

        assert isinstance(data, list)
        assert len(data) >= 2
        assert data[0]["title"] == "Learn Docker"
        assert data[1]["title"] == "Learn Kubernetes"

def test_create_task_without_title(client):
        response = client.post(
                "/tasks",
                json={}
        )

        assert response.status_code == 400

def test_create_task_with_empty_title(client):
        response = client.post(
                "/tasks",
                json={"title": ""}
        )

        assert response.status_code == 400

def test_create_task_with_invalid_title_type(client):
        response = client.post(
                "/tasks",
                json={"title": 123}
        )

        assert response.status_code == 400

def test_create_task_strips_title_whitespace(client):
        response = client.post(
                "/tasks",
                json={"title": "   Learn Jenkins   "}
        )

        assert response.status_code == 201

        data = response.get_json()

        assert data["title"] == "Learn Jenkins"
