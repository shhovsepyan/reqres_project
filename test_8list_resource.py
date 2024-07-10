import json
import requests
import pytest
import allure

import test_1register
import test_3login_user


@allure.feature("TEST REQRES.IN")
@allure.suite("TEST NEW PROJECT")
@allure.title("Test list resource")
@allure.description("This test case verifies listing all resources")
@pytest.mark.smoke
def test_list_resource():
    request_url = test_1register.base_url + "api/unknown"
    headers = {
        'token': test_3login_user.authorization_token
    }

    with allure.step("Send GET request to list resources"):
        response = requests.get(request_url, headers=headers)
        print(response)

    with allure.step("Verify response status code is 200"):
        assert response.status_code == 200, f'Expected Status Code 200, but got {response.status_code}'

    with allure.step("Parse and print response data"):
        response_data = response.json()
        json_str = json.dumps(response_data, indent=4)
        print(json_str)

    with allure.step("Verify JSON structure of response data"):
        assert "page" in response_data and isinstance(response_data["page"], int)
        assert "per_page" in response_data and isinstance(response_data["per_page"], int)
        assert "total" in response_data and isinstance(response_data["total"], int)
        assert "total_pages" in response_data and isinstance(response_data["total_pages"], int)
        assert "data" in response_data and isinstance(response_data["data"], list)
        assert len(response_data["data"]) == 6

        # Check each item in data list for expected structure
        for item in response_data["data"]:
            assert "id" in item and isinstance(item["id"], int)
            assert "name" in item and isinstance(item["name"], str)
            assert "year" in item and isinstance(item["year"], int)
            assert "color" in item and isinstance(item["color"], str)
            assert "pantone_value" in item and isinstance(item["pantone_value"], str)

    with allure.step("Verify support section in response data"):
        assert "support" in response_data and isinstance(response_data["support"], dict)
        assert "url" in response_data["support"] and isinstance(response_data["support"]["url"], str)
        assert "text" in response_data["support"] and isinstance(response_data["support"]["text"], str)
