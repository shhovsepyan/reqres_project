import json
import requests
import pytest
import allure

import test_1register
import test_3login_user


@allure.feature("TEST REQRES.IN")
@allure.suite("TEST NEW PROJECT")
@allure.title("Test list all users")
@allure.description("This test case verifies listing all users on page 2")
@pytest.mark.smoke
def test_list_all_users():
    request_url = test_1register.base_url + "api/users?page=2"
    headers = {
        'token': test_3login_user.authorization_token
    }

    with allure.step("Send GET request to list all users"):
        response = requests.get(request_url, headers=headers)
        print(response)

    with allure.step("Verify response status code is 200"):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step("Parse and print response data"):
        response_data = response.json()
        json_str = json.dumps(response_data, indent=4)
        print(json_str)
