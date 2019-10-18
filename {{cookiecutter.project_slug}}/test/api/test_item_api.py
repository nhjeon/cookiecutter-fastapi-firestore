from starlette.testclient import TestClient

from app.main import app

CLIENT = TestClient(app)


def test_create_item_api():
    response = CLIENT.get("/items")
    assert response.status_code == 403
