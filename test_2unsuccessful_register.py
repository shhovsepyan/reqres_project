import json
import requests
import pytest
import allure

base_url = "https://reqres.in/"


@allure.feature("TEST REQRES.IN")
@allure.suite("TEST NEW PROJECT")
@allure.title("Test unsuccessful registration")
@allure.description("This test case verifies that registration fails when the password is missing")
@pytest.mark.smoke
def test_unsuccessful_registration():
    body = {
        "email": "sydney@fife"
    }
    headers = {'Content-Type': 'application/json'}
    request_url = base_url + 'api/register'

    with allure.step("Send POST request to register user without password"):
        post_response = requests.post(request_url, json=body, headers=headers)

    with allure.step("Parse response data"):
        response_data = post_response.json()

    with allure.step("Verify response contains 'Missing password' error"):
        assert response_data['error'] == 'Missing password'

    with allure.step("Verify response status code is 400"):
        assert post_response.status_code == 400, f'Expected Status Code 400, but got {post_response.status_code}'
