from registration.api import APIActions
from registration.models import Item

URL = "https://stores-tests-api.herokuapp.com"


class TestStoreItem:

    TOKEN = APIActions(url=URL).get_access_token()
    HEADERS = {
        "Authorization": f"JWT {TOKEN}",
    }

    ITEM = None
    ITEM_NAME = None

    def test_add_new_item(self):

        TestStoreItem.ITEM = Item.random_body()
        TestStoreItem.ITEM_NAME = Item.random_name()
        response = APIActions(url=URL).create_item(body=TestStoreItem.ITEM, name=TestStoreItem.ITEM_NAME,
                                                   headers=self.HEADERS)

        assert response.status == 201
        assert response.response.get("name") == TestStoreItem.ITEM_NAME
        assert response.response.get("price") == float(TestStoreItem.ITEM["price"])
        assert response.response.get("description") == TestStoreItem.ITEM["description"]
        assert response.response.get("image") == TestStoreItem.ITEM["image"]

    def test_change_item(self):
        TestStoreItem.ITEM_NAME = Item.random_name()
        response = APIActions(url=URL).create_item(body=TestStoreItem.ITEM, name=TestStoreItem.ITEM_NAME,
                                                   headers=self.HEADERS)

        assert response.status == 201
        assert response.response.get("name") == TestStoreItem.ITEM_NAME
        assert response.response.get("price") == float(TestStoreItem.ITEM["price"])
        assert response.response.get("description") == TestStoreItem.ITEM["description"]
        assert response.response.get("image") == TestStoreItem.ITEM["image"]

    def test_get_item(self):
        response = APIActions(url=URL).get_item(name=TestStoreItem.ITEM_NAME, headers=self.HEADERS)

        assert response.status == 200
        assert response.response.get("name") == TestStoreItem.ITEM_NAME
        assert response.response.get("price") == float(TestStoreItem.ITEM["price"])
        assert response.response.get("description") == TestStoreItem.ITEM["description"]
        assert response.response.get("image") == TestStoreItem.ITEM["image"]

