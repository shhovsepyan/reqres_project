import json
import requests
import pytest
import allure
import test_1register
from test_1register import base_url

authorization_token = None


@allure.feature("TEST REQRES.IN")
@allure.suite("TEST NEW PROJECT")
@allure.title("Test login user")
@allure.description("This test case verifies logging in a user with valid credentials")
@pytest.mark.smoke
def test_login_user():
    request_url = base_url + "api/login"

    body = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step("Send POST request to login user"):
        post_response = requests.post(request_url, json=body, headers=headers)
        print(post_response)

    with allure.step("Parse response data"):
        response_data = post_response.json()
        json_str = json.dumps(response_data, indent=4)
        print(json_str)

    with allure.step("Verify response status code is 200"):
        assert post_response.status_code == 200, f'Expected Status Code 200, but got {post_response.status_code}'

    with allure.step("Extract and verify authorization token"):
        global authorization_token
        authorization_token = response_data['token']
        assert authorization_token is not None, 'Authorization token is not provided'
