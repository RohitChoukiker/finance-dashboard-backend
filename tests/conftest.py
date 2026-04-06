import pytest
import random
from fastapi.testclient import TestClient
from main import app




def get_random_email():
    return f"user{random.randint(1000,9999)}@test.com"


@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def disable_rate_limit():
    app.state.limiter.enabled = False


@pytest.fixture
def user_token(client):
    email = get_random_email()

    client.post("/auth/signup", json={
        "name": "Test User",
        "email": email,
        "password": "123456"
    })

    res = client.post("/auth/login", json={
        "email": email,
        "password": "123456"
    })

    return res.json()["data"]["access_token"]



@pytest.fixture
def admin_token(client):
    res = client.post("/auth/login", json={
        "email": "admin@gmail.com",
        "password": "admin123"
    })
    return res.json()["data"]["access_token"]