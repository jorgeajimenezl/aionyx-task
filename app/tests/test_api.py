from starlette.testclient import TestClient
from app.api import app

client = TestClient(app)


def test_completation():
    request_body = {
        "prompt": "Hello, my name is Jorge, Who are you?",
        "vendor": "openai",
        "model": "gpt-3.5-turbo",
        "temperature": 0.7,
    }
    response = client.post("/completation", json=request_body)
    assert response.status_code == 200
    assert "response" in response.json()


def test_completation_vendor_error():
    request_body = {
        "prompt": "Hi!",
        "vendor": "123456789",
        "model": "gpt-3.5-turbo",
        "temperature": 0.7,
    }
    response = client.post("/completation", json=request_body)
    assert response.status_code == 404
    assert "detail" in response.json()


def test_vendors():
    response = client.get("/vendors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
