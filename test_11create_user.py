import json
import requests
import pytest
import allure

import test_1register
import test_3login_user

data = {
    "name": "morpheus",
    "job": "leader"
}


@allure.feature("TEST REQRES.IN")
@allure.suite("TEST NEW PROJECT")
@allure.title("Test create user")
@allure.description("This test case verifies creating a new user")
@pytest.mark.smoke
def test_create_user():
    request_url = test_1register.base_url + "api/users"
    headers = {
        'token': test_3login_user.authorization_token
    }

    with allure.step("Send POST request to create user"):
        response = requests.post(request_url, headers=headers, json=data)
        print(response)

    with allure.step("Verify response status code is 201"):
        assert response.status_code == 201, f'Expected Status Code 201, but got {response.status_code}'

    with allure.step("Parse and assert response data"):
        response_data = response.json()
        assert "name" in response_data, "Response does not contain 'name' field"
        assert response_data["name"] == "morpheus", f"Expected 'name' to be 'morpheus', but got {response_data['name']}"
        assert "job" in response_data, "Response does not contain 'job' field"
        assert response_data["job"] == "leader", f"Expected 'job' to be 'leader', but got {response_data['job']}"
        assert "id" in response_data, "Response does not contain 'id' field"
        assert isinstance(response_data["id"], str), "Expected 'id' to be a string"
        assert "createdAt" in response_data, "Response does not contain 'createdAt' field"

    with allure.step("Print the created user information"):
        print("Created user:")
        print(json.dumps(response_data, indent=4))
