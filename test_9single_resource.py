import json
import requests
import pytest
import allure

import test_1register
import test_3login_user


@allure.feature("TEST REQRES.IN")
@allure.suite("TEST NEW PROJECT")
@allure.title("Test single resource")
@allure.description("This test case verifies retrieving a single resource by ID")
@pytest.mark.smoke
def test_single_resource():
    request_url = test_1register.base_url + "api/unknown/2"
    headers = {
        'token': test_3login_user.authorization_token
    }

    with allure.step("Send GET request to retrieve single resource"):
        response = requests.get(request_url, headers=headers)
        print(response)

    with allure.step("Verify response status code is 200"):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step("Parse and print response data"):
        response_data = response.json()
        json_str = json.dumps(response_data, indent=4)
        print(json_str)

    with allure.step("Verify JSON structure of response data"):
        assert "data" in response_data, "Missing 'data' key in response"
        assert isinstance(response_data["data"], dict), "'data' should be a dictionary"
        assert response_data["data"]["id"] == 2, f"Expected 'id' to be 2, but got {response_data['data']['id']}"
        assert response_data["data"][
                   "name"] == "fuchsia rose", f"Expected 'name' to be 'fuchsia rose', but got {response_data['data']['name']}"
        assert response_data["data"][
                   "year"] == 2001, f"Expected 'year' to be 2001, but got {response_data['data']['year']}"
        assert response_data["data"][
                   "color"] == "#C74375", f"Expected 'color' to be '#C74375', but got {response_data['data']['color']}"
        assert response_data["data"][
                   "pantone_value"] == "17-2031", f"Expected 'pantone_value' to be '17-2031', but got {response_data['data']['pantone_value']}"

    with allure.step("Verify support section in response data"):
        assert "support" in response_data, "Missing 'support' key in response"
        assert isinstance(response_data["support"], dict), "'support' should be a dictionary"
        assert response_data["support"][
                   "url"] == "https://reqres.in/#support-heading", f"Expected 'url' to be 'https://reqres.in/#support-heading', but got {response_data['support']['url']}"
        assert response_data["support"][
                   "text"] == "To keep ReqRes free, contributions towards server costs are appreciated!", f"Expected 'text' to be 'To keep ReqRes free, contributions towards server costs are appreciated!', but got {response_data['support']['text']}"
