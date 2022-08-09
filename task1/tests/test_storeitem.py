from registration.api import Auth, StoreItem
from registration.models import Item

URL = "https://stores-tests-api.herokuapp.com"


class TestStoreItem:
    TOKEN = Auth(url=URL) \
        .get_access_token(register_url=URL).json()["access_token"]

    def test_add_new_item(self):
        body = Item.random_body()
        self.name = Item.random_name()
        response = StoreItem(url=URL).post_item(body=body, name=self.name)

        assert response.status == 200
        assert response.response.get("name") == self.name

    def test_change_item(self):
        body = Item.random_body()
        self.name = Item.random_name()
        response = StoreItem(url=URL).post_item(body=body, name=self.name)

        assert response.status == 200
        assert response.response.get("name") == self.name

    def test_get_tem(self):
        response = StoreItem(url=URL).get_item(name=self.name)

        assert response.status == 200
        assert response.response.get("name") == self.name

