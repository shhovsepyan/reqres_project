import json
import requests
import pytest
import allure

import test_1register
import test_3login_user


@allure.feature("TEST REQRES.IN")
@allure.suite("TEST NEW PROJECT")
@allure.title("Test delete user")
@allure.description("This test case verifies deleting a user")
@pytest.mark.smoke
def test_delete_user():
    request_url = test_1register.base_url + "api/users/2"
    headers = {
        'token': test_3login_user.authorization_token
    }

    with allure.step("Send DELETE request to delete user"):
        response = requests.delete(request_url, headers=headers)
        print(response)
        assert response.status_code == 204, f"Expected status code 204, but got {response.status_code}"

    with allure.step("Verify user deletion by sending a GET request"):
        check_response = requests.get(request_url)

        assert check_response.status_code == 404, f"Expected status code 404, but got {check_response.status_code}"

    with allure.step("Print confirmation message"):
        print("User deleted successfully")
