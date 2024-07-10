import json
import requests
import pytest
import allure

import test_1register
import test_3login_user

data = {
    "name": "morpheus",
    "job": "zion resident"
}


@allure.feature("TEST REQRES.IN")
@allure.suite("TEST NEW PROJECT")
@allure.title("Test update user (PUT)")
@allure.description("This test case verifies updating a user using PUT method")
@pytest.mark.smoke
def test_update_user():
    request_url = test_1register.base_url + "api/users/2"
    headers = {
        'token': test_3login_user.authorization_token
    }

    with allure.step("Send PUT request to update user"):
        response = requests.put(request_url, headers=headers, json=data)
        print(response)

    with allure.step("Verify response status code is 200"):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step("Parse and assert response data"):
        response_data = response.json()
        assert "name" in response_data, "Response does not contain 'name' field"
        assert response_data["name"] == "morpheus", f"Expected 'name' to be 'morpheus', but got {response_data['name']}"

        assert "job" in response_data, "Response does not contain 'job' field"
        assert response_data[
                   "job"] == "zion resident", f"Expected 'job' to be 'zion resident', but got {response_data['job']}"

        assert "updatedAt" in response_data, "Response does not contain 'updatedAt' field"

    with allure.step("Print the updated user information"):
        print("Updated user:")
        print(json.dumps(response_data, indent=4))
