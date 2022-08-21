from factory.item_factory import ItemFactory
from registration.api import APIActions

URL = "https://stores-tests-api.herokuapp.com"


class TestStoreItem:

    TOKEN = APIActions(url=URL).get_access_token()
    HEADERS = {
        "Authorization": f"JWT {TOKEN}",
    }

    ITEM = None

    def test_add_new_item(self):

        TestStoreItem.ITEM = ItemFactory().create_item()
        body = TestStoreItem.ITEM.as_dict()
        response = APIActions(url=URL).create_item(body=body, name=TestStoreItem.ITEM.name,
                                                   headers=self.HEADERS)

        assert response.status == 201
        assert response.response.get("itemID")
        assert response.response.get("name") == TestStoreItem.ITEM.name
        assert response.response.get("price") == float(body["price"])
        assert response.response.get("description") == body["description"]
        assert response.response.get("image") == body["image"]

    def test_change_item(self):
        TestStoreItem.ITEM.name = ItemFactory().new_name()
        body = TestStoreItem.ITEM.as_dict()
        response = APIActions(url=URL).create_item(body=body, name=TestStoreItem.ITEM.name,
                                                   headers=self.HEADERS)

        assert response.status == 201
        assert response.response.get("itemID")
        assert response.response.get("name") == TestStoreItem.ITEM.name
        assert response.response.get("price") == float(body["price"])
        assert response.response.get("description") == body["description"]
        assert response.response.get("image") == body["image"]

    def test_get_item(self):
        body = TestStoreItem.ITEM.as_dict()
        response = APIActions(url=URL).get_item(name=TestStoreItem.ITEM.name, headers=self.HEADERS)

        assert response.status == 200
        assert response.response.get("itemID")
        assert response.response.get("name") == TestStoreItem.ITEM.name
        assert response.response.get("price") == float(body["price"])
        assert response.response.get("description") == body["description"]
        assert response.response.get("image") == body["image"]
