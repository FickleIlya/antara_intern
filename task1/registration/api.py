import logging
from jsonschema import validate

from registration.request import Client
from registration.models import ResponseModel, RegisterUser
from schemas.registration import valid_schema

logger = logging.getLogger("api")


class Register:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    POST_REGISTER_USER = '/register'

    def register_user(self, body: dict, schema: dict):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser
        """
        response = self.client.custom_request("POST", f"{self.url}{self.POST_REGISTER_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())


class Auth:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    POST_REGISTERED_USER = '/auth'

    def get_access_token(self, register_url: str):
        body = RegisterUser.random()
        Register(url=register_url).register_user(body=body, schema=valid_schema)
        response = self.client.custom_request("POST", f"{self.url}{self.POST_REGISTERED_USER}", json=body)
        return response


class StoreItem:

    def __init__(self, url):
        self.url = url
        self.client = Client()

    STORE_ITEM = "/item/"

    def post_item(self, body: dict, name: str):
        response = self.client.custom_request("POST", f"{self.url}{self.STORE_ITEM}{name}", json=body)

        return ResponseModel(status=response.status_code, response=response.json())

    def change_item(self, body: dict, name: str):
        response = self.client.custom_request("PUT", f"{self.url}{self.STORE_ITEM}{name}", json=body)

        return ResponseModel(status=response.status_code, response=response.json())

    def get_item(self, name: str):
        response = self.client.custom_request("GET", f"{self.url}{self.STORE_ITEM}{name}")

        return ResponseModel(status=response.status_code, response=response.json())
