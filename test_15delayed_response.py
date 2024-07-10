import json
import requests
import pytest
import allure

import test_1register
import test_3login_user


@allure.feature("TEST REQRES.IN")
@allure.suite("TEST NEW PROJECT")
@allure.title("Test delayed response")
@allure.description("This test case verifies delayed response for fetching users")
@pytest.mark.smoke
def test_delayed_response():
    request_url = test_1register.base_url + "api/users?delay=3"
    headers = {
        'token': test_3login_user.authorization_token
    }

    with allure.step("Send GET request to fetch users with delay"):
        response = requests.get(request_url, headers=headers)
        print(response)

    with allure.step("Verify response status code is 200"):
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    with allure.step("Parse and assert response data structure"):
        response_data = response.json()
        assert "page" in response_data, "Response does not contain 'page' field"
        assert "per_page" in response_data, "Response does not contain 'per_page' field"
        assert "total" in response_data, "Response does not contain 'total' field"
        assert "total_pages" in response_data, "Response does not contain 'total_pages' field"
        assert "data" in response_data, "Response does not contain 'data' field"
        assert "support" in response_data, "Response does not contain 'support' field"

    with allure.step("Assert specific fields within the 'support' object"):
        assert "url" in response_data["support"], "Support object does not contain 'url' field"
        assert "text" in response_data["support"], "Support object does not contain 'text' field"

    with allure.step("Assert pagination details"):
        assert response_data["page"] == 1, f"Expected page 1, but got {response_data['page']}"
        assert response_data["per_page"] == 6, f"Expected per_page 6, but got {response_data['per_page']}"
        assert response_data["total"] == 12, f"Expected total 12, but got {response_data['total']}"
        assert response_data["total_pages"] == 2, f"Expected total_pages 2, but got {response_data['total_pages']}"

    with allure.step("Assert that 'data' field is a list and contains at least one user"):
        assert isinstance(response_data["data"], list), "Expected 'data' to be a list"
        assert len(response_data["data"]) > 0, "Expected 'data' to contain at least one user"

    # Print the list of users
    print("List of Users:")
    for user in response_data["data"]:
        print(f"{user['first_name']} {user['last_name']}")
