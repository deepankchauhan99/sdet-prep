import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)
assert response.status_code == 200, "Status code is not 200"

data = response.json()

print("Number of users:", len(data))


assert len(data) > 0, "User list is empty"

for user in data:
    assert "email" in user, "Email field missing"

print("API test passed successfully")

# Added function structure for the same thing as above
def test_users_api():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    assert response.status_code == 200

    data = response.json()

    assert len(data) > 0
