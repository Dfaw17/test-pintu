import pytest
import requests
from assertpy import assert_that
from setting import Locator as L


@pytest.mark.api
class TestAutomationPintuApiGet:

    def test_get_api(self):
        get_data = requests.get(L.url_api)

        validate_userId = get_data.json()[1].get("userId")
        validate_Id = get_data.json()[1].get("id")
        validate_title = get_data.json()[1].get("title")
        validate_body = get_data.json()[1].get("body")
        validate_response_code = get_data.status_code

        assert_that(validate_response_code).is_equal_to(200)
        assert_that(validate_userId).is_type_of(int)
        assert_that(validate_Id).is_type_of(int)
        assert_that(validate_title).is_type_of(str)
        assert_that(validate_body).is_type_of(str)
        assert_that([validate_userId, validate_Id, validate_body, validate_title]).is_not_none()

        print("triggred3")
