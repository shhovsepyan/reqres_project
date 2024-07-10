import json
import requests
import pytest
import allure

import test_1register

@allure.feature("TEST REQRES.IN")
@allure.suite("TEST NEW PROJECT")
@allure.title("Test unsuccessful login")
@allure.description("This test case verifies that login fails when the password is missing")
@pytest.mark.smoke
def test_unsuccessful_login():
    request_url = test_1register.base_url + "api/login"

    body = {
        "email": "peter@klaven",
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step("Send POST request to login user without password"):
        post_response = requests.post(request_url, json=body, headers=headers)
        print(post_response)

    with allure.step("Parse response data"):
        response_data = post_response.json()

    with allure.step("Verify response contains 'Missing password' error"):
        assert response_data['error'] == 'Missing password'

    with allure.step("Verify response status code is 400"):
        assert post_response.status_code == 400, f'Expected Status Code 400, but got {post_response.status_code}'
