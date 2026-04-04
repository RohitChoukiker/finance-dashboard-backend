import random
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def get_random_email():
    return f"user{random.randint(1000,9999)}@test.com"


def test_signup():
    email = get_random_email()

    response = client.post("/auth/signup", json={
        "name": "Test User",
        "email": email,
        "password": "123456"
    })

    assert response.status_code == 200
    assert response.json()["message"] == "User created successfully"


def test_login():
    email = get_random_email()

   
    client.post("/auth/signup", json={
        "name": "Test User",
        "email": email,
        "password": "123456"
    })

    
    response = client.post("/auth/login", json={
        "email": email,
        "password": "123456"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()["data"]


def test_get_me():
    email = get_random_email()


    client.post("/auth/signup", json={
        "name": "Test User",
        "email": email,
        "password": "123456"
    })

   
    login_res = client.post("/auth/login", json={
        "email": email,
        "password": "123456"
    })

    token = login_res.json()["data"]["access_token"]


    response = client.get(
        "/auth/me",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert response.json()["data"]["email"] == email


def test_invalid_login():
    response = client.post("/auth/login", json={
        "email": "wrong@test.com",
        "password": "wrongpass"
    })

    assert response.status_code != 200


def test_admin_login():
    response = client.post("/auth/login", json={
        "email": "admin@gmail.com",
        "password": "admin123"
    })

    assert response.status_code == 200
    assert "access_token" in response.json()["data"]
    

def test_get_users():
    login_res = client.post("/auth/login", json={
        "email": "admin@gmail.com",
        "password": "admin123"
    })

    token = login_res.json()["data"]["access_token"]

    response = client.get(
        "/auth/users",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert "data" in response.json()



def test_users_count():
    login_res = client.post("/auth/login", json={
        "email": "admin@gmail.com",
        "password": "admin123"
    })

    token = login_res.json()["data"]["access_token"]

    response = client.get(
        "/auth/users/count",
        headers={"Authorization": f"Bearer {token}"}
    )

    assert response.status_code == 200
    assert "total_users" in response.json()["data"]



def test_change_role():
    email = get_random_email()


    client.post("/auth/signup", json={
        "name": "User",
        "email": email,
        "password": "123456"
    })

  
    admin_login = client.post("/auth/login", json={
        "email": "admin@gmail.com",
        "password": "admin123"
    })

    admin_token = admin_login.json()["data"]["access_token"]


    users_res = client.get(
        "/auth/users",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    user_id = users_res.json()["data"][-1]["id"]

    response = client.put(
        f"/auth/users/{user_id}/role?role=analyst",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200


def test_update_status():
    email = get_random_email()

    
    client.post("/auth/signup", json={
        "name": "User",
        "email": email,
        "password": "123456"
    })


    admin_login = client.post("/auth/login", json={
        "email": "admin@gmail.com",
        "password": "admin123"
    })

    admin_token = admin_login.json()["data"]["access_token"]

 
    users_res = client.get(
        "/auth/users",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    user_id = users_res.json()["data"][-1]["id"]

   
    response = client.put(
        f"/auth/users/{user_id}/status?is_active=false",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 200

    
    

