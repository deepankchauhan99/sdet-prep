import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users():
    response = requests.get(f"{BASE_URL}/users")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0

def test_user_has_email():
    response = requests.get(f"{BASE_URL}/users")

    data = response.json()

    for user in data:
        assert "email" in user

def test_user_id_exists():
    response = requests.get(f"{BASE_URL}/users")
    data = response.json()

    for user in data:
        assert user["id"] > 0