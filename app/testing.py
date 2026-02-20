import json
from urllib.parse import urlencode

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User


class AuthTokenTesting(APITestCase):
    schema = None

    def get_logged_user(self):
        email, password = "test@user.com", "nonsecurepassword4Tests"
        user = User.objects.create_user(email, password)
        self.client.login(email=email, password=password)
        return user

    @staticmethod
    def get_access_token(user):
        """
        Obtain Token for User
        """
        return str(RefreshToken.for_user(user).access_token)

    def get(self, url, expected_status, token=None, params=None):
        """
        GET method with access token
        """
        kwargs = {}
        if token:
            kwargs["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        if params:
            kwargs["QUERY_STRING"] = urlencode(params, doseq=True)
        response = self.client.get(url, **kwargs)
        self.assertEqual(response.status_code, expected_status, str(response))
        if hasattr(response, "data"):
            return response.data
        else:
            return response

    def post(self, url, data, expected_status, token=None):
        """
        POST method with access token
        """
        kwargs = {"content_type": "application/json"}
        if token:
            kwargs["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        response = self.client.post(url, json.dumps(data), **kwargs)
        self.assertEqual(response.status_code, expected_status, str(response))
        return response.data

    def patch(self, url, data, expected_status, token):
        """
        PATCH method with access token
        """
        kwargs = {"content_type": "application/json"}
        if token:
            kwargs["HTTP_AUTHORIZATION"] = f"Bearer {token}"
        response = self.client.patch(url, json.dumps(data), **kwargs)
        self.assertEqual(response.status_code, expected_status, response.data)
        return response.data

    def validate_schema(self, data):
        if self.schema is None:
            raise Exception("Schema is not defined")

        if isinstance(data, list):
            return [self.schema(**item) for item in data]
        return self.schema(**data)

    def assert_status_200(self, response):
        self.assertEqual(response.status_code, status.HTTP_200_OK, response.data)

    def assert_status_201(self, response):
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)

    def assert_status_403(self, response):
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN, response.data)

    def assert_status_400(self, response):
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST, response.data)
