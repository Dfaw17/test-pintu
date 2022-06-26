import pytest
import requests
from assertpy import assert_that
from data import Data as D
from setting import Locator as L


@pytest.mark.api
class TestAutomationPintuApiPost:

    def test_post_api_normal(self):

        data = {
            "title": D.title,
            "body": D.body,
            "userId": int(D.userId)
        }

        post_data = requests.post(L.url_api, data=data)

        validate_title = post_data.json().get("title")
        validate_body = post_data.json().get("body")
        validate_userId = int(post_data.json().get("userId"))

        assert_that(post_data.status_code).is_equal_to(201)
        assert_that(validate_title).is_equal_to(D.title)
        assert_that(validate_body).is_equal_to(D.body)
        assert_that(validate_userId).is_equal_to(D.userId)

    def test_post_api_data_null(self):

        data = {
            "title": D.title_emp,
            "body": D.body_emp,
            "userId": D.userId_emp
        }

        post_data = requests.post(L.url_api, data=data)

        validate_title = post_data.json().get("title")
        validate_body = post_data.json().get("body")
        validate_userId = post_data.json().get("userId")

        assert_that(validate_title).is_equal_to(D.title_emp)
        assert_that(validate_body).is_equal_to(D.body_emp)
        assert_that(validate_userId).is_equal_to(D.userId_emp)

    def test_post_api_user_id_string(self):

        data = {
            "title": D.title,
            "body": D.body,
            "userId": D.userId_str
        }

        post_data = requests.post(L.url_api, data=data)

        validate_title = post_data.json().get("title")
        validate_body = post_data.json().get("body")
        validate_userId = post_data.json().get("userId")

        assert_that(validate_title).is_equal_to(D.title)
        assert_that(validate_body).is_equal_to(D.body)
        assert_that(validate_userId).is_equal_to(D.userId_str)
