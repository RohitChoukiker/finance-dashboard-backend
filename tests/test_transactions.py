from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_transaction(user_token):
    res = client.post(
        "/transactions",
        json={
            "amount": 1000,
            "type": "income",
            "category": "salary"
        },
        headers={"Authorization": f"Bearer {user_token}"}
    )

    assert res.status_code == 200
    assert res.json()["message"] == "Transaction created"


def test_get_transactions(user_token):
    res = client.get(
        "/transactions",
        headers={"Authorization": f"Bearer {user_token}"}
    )

    assert res.status_code == 200
    assert "data" in res.json()


def test_get_single_transaction(user_token):
    create = client.post(
        "/transactions",
        json={"amount": 2000, "type": "income"},
        headers={"Authorization": f"Bearer {user_token}"}
    )

    tx_id = create.json()["data"]["id"]

    res = client.get(
        f"/transactions/{tx_id}",
        headers={"Authorization": f"Bearer {user_token}"}
    )

    assert res.status_code == 200
    assert res.json()["id"] == tx_id


def test_update_transaction(user_token):
    create = client.post(
        "/transactions",
        json={"amount": 1000, "type": "income"},
        headers={"Authorization": f"Bearer {user_token}"}
    )

    tx_id = create.json()["data"]["id"]

    res = client.put(
        f"/transactions/{tx_id}",
        json={"amount": 3000, "type": "expense"},
        headers={"Authorization": f"Bearer {user_token}"}
    )

    assert res.status_code == 200
    assert res.json()["message"] == "Transaction updated"


def test_delete_transaction(user_token):
    create = client.post(
        "/transactions",
        json={"amount": 1000, "type": "income"},
        headers={"Authorization": f"Bearer {user_token}"}
    )

    tx_id = create.json()["data"]["id"]

    res = client.delete(
        f"/transactions/{tx_id}",
        headers={"Authorization": f"Bearer {user_token}"}
    )

    assert res.status_code == 200
    assert res.json()["message"] == "Transaction deleted"


def test_dashboard_summary(user_token):
    res = client.get(
        "/transactions/dashboard/summary",
        headers={"Authorization": f"Bearer {user_token}"}
    )

    assert res.status_code == 200
    assert "data" in res.json()