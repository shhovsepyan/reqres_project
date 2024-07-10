import json
import requests
import pytest
import allure

base_url = "https://reqres.in/"
authorization_token = None


@allure.feature("TEST REQRES.IN")
@allure.suite("TEST NEW PROJECT")
@allure.title("Test register user")
@allure.description("This test case verifies registering user")
@pytest.mark.smoke
def test_register_user():
    body = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    headers = {'Content-Type': 'application/json'}
    request_url = base_url + 'api/register'

    with allure.step("Send POST request to register user"):
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
