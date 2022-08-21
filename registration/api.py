import logging
from jsonschema import validate

from registration.request import Client
from registration.models import ResponseModel, RegisterUser
from schemas.registration import valid_schema
from typing import Optional
logger = logging.getLogger("api")


class APIActions:
    POST_REGISTER_USER = '/register'
    AUTH_USER = '/auth'
    STORE_ITEM = "/item/"

    def __init__(self, url):
        self.url = url
        self.client = Client()

    # Register
    def register_user(self, body: dict, schema: dict):
        """
        https://app.swaggerhub.com/apis-docs/berpress/flask-rest-api/1.0.0#/register/regUser
        """
        response = self.client.custom_request("POST", f"{self.url}{self.POST_REGISTER_USER}", json=body)
        validate(instance=response.json(), schema=schema)
        logger.info(response.text)
        return ResponseModel(status=response.status_code, response=response.json())

    # Auth
    def get_access_token(self, body: Optional[dict] = None):
        if not body:
            body = RegisterUser.random()
            self.register_user(body=body, schema=valid_schema)

        response = self.client.custom_request("POST", f"{self.url}{self.AUTH_USER}", json=body)
        return response.json()["access_token"]

    # StoreItem
    def create_item(self, body: dict, name: str, headers: dict):
        response = self.client.custom_request("POST", f"{self.url}{self.STORE_ITEM}{name}", json=body, headers=headers)

        return ResponseModel(status=response.status_code, response=response.json())

    def change_item(self, body: dict, name: str, headers: dict):
        response = self.client.custom_request("PUT", f"{self.url}{self.STORE_ITEM}{name}", json=body, headers=headers)

        return ResponseModel(status=response.status_code, response=response.json())

    def get_item(self, name: str, headers: dict):
        response = self.client.custom_request("GET", f"{self.url}{self.STORE_ITEM}{name}", headers=headers)

        return ResponseModel(status=response.status_code, response=response.json())
