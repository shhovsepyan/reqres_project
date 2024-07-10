import json
import requests
import pytest
import allure

import test_1register
import test_3login_user

@allure.feature("TEST REQRES.IN")
@allure.suite("TEST NEW PROJECT")
@allure.title("Test single user not found")
@allure.description("This test case verifies the behavior when a single user is not found (user ID 23)")
@pytest.mark.smoke
def test_list_single_user_not_found():
    request_url = test_1register.base_url + "api/users/23"
    headers = {
        'token': test_3login_user.authorization_token
    }

    with allure.step("Send GET request to retrieve non-existing user"):
        response = requests.get(request_url, headers=headers)
        print(response)

    with allure.step("Verify response status code is 404"):
        assert response.status_code == 404, f'Expected Status Code 404, but got {response.status_code}'

    with allure.step("Parse and print response data"):
        response_data = response.json()
        print(response_data)
        json_str = json.dumps(response_data, indent=4)
        print(json_str)

    with allure.step("Verify response data is an empty dictionary"):
        assert response_data == {}, "Expected an empty dictionary when no data is found"
