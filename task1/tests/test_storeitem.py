from registration.api import Auth, StoreItem
from registration.models import Item

URL = "https://stores-tests-api.herokuapp.com"

TOKEN = Auth(url=URL) \
        .get_access_token(register_url=URL).json()["access_token"]

HEADERS = {
        "Authorization": f"JWT {TOKEN}",
    }

NAME = ""


class TestStoreItem:

    def test_add_new_item(self):
        body = Item.random_body()
        global NAME
        NAME = Item.random_name()
        response = StoreItem(url=URL).post_item(body=body, name=NAME, headers=HEADERS)

        # assert NAME is str
        assert response.status == 200
        assert response.response.get("name") == NAME

    def test_change_item(self):
        body = Item.random_body()
        global NAME
        NAME = Item.random_name()
        response = StoreItem(url=URL).post_item(body=body, name=NAME, headers=HEADERS)
        # assert NAME is str
        assert response.status == 200
        assert response.response.get("name") == NAME

    def test_get_tem(self):
        response = StoreItem(url=URL).get_item(name=NAME, headers=HEADERS)
        # assert NAME is str
        assert response.status == 200
        assert response.response.get("name") == NAME

