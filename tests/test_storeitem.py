from registration.api import Auth, StoreItem
from registration.models import Item

URL = "https://stores-tests-api.herokuapp.com"

NAME = Item.random_name()


class TestStoreItem:

    TOKEN = Auth(url=URL) \
        .get_access_token(register_url=URL).json()["access_token"]

    HEADERS = {
        "Authorization": f"JWT {TOKEN}",
    }

    def test_add_new_item(self):

        body = Item.random_body()
        response = StoreItem(url=URL).post_item(body=body, name=NAME, headers=self.HEADERS)
        assert response.status == 201
        assert response.response.get("name") == NAME

    def test_change_item(self):
        global NAME

        body = Item.random_body()
        new_name = Item.random_name()
        NAME = new_name
        response = StoreItem(url=URL).post_item(body=body, name=new_name, headers=self.HEADERS)

        assert response.status == 201
        assert response.response.get("name") == new_name

    def test_get_item(self):
        response = StoreItem(url=URL).get_item(name=NAME, headers=self.HEADERS)
        assert response.status == 200
        assert response.response.get("name") == NAME

