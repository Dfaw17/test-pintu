import pytest
import requests
from assertpy import assert_that
from pytest_steps import test_steps

from setting import Locator as L


@pytest.mark.api
class TestAutomationPintuApiPost:

    def test_post_api_normal(self):
        title = "halo"
        body = "halo body"
        userId = 7
        data = {
            "title": title,
            "body": body,
            "userId": int(userId)
        }

        post_data = requests.post(L.url_api, data=data)

        validate_title = post_data.json().get("title")
        validate_body = post_data.json().get("body")
        validate_userId = int(post_data.json().get("userId"))

        assert_that(post_data.status_code).is_equal_to(201)
        assert_that(validate_title).is_equal_to(title)
        assert_that(validate_body).is_equal_to(body)
        assert_that(validate_userId).is_equal_to(userId)

    def test_post_api_data_null(self):
        title = ""
        body = ""
        userId = ""

        data = {
            "title": title,
            "body": body,
            "userId": userId
        }

        post_data = requests.post(L.url_api, data=data)

        validate_title = post_data.json().get("title")
        validate_body = post_data.json().get("body")
        validate_userId = post_data.json().get("userId")

        assert_that(validate_title).is_equal_to(title)
        assert_that(validate_body).is_equal_to(body)
        assert_that(validate_userId).is_equal_to(userId)

    def test_post_api_user_id_string(self):
        title = "halo"
        body = "halo body"
        userId = "7"

        data = {
            "title": title,
            "body": body,
            "userId": userId
        }

        post_data = requests.post(L.url_api, data=data)

        validate_title = post_data.json().get("title")
        validate_body = post_data.json().get("body")
        validate_userId = post_data.json().get("userId")

        assert_that(validate_title).is_equal_to(title)
        assert_that(validate_body).is_equal_to(body)
        assert_that(validate_userId).is_equal_to(userId)
