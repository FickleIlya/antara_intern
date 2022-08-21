from faker import Faker
import random

fake = Faker()


class RegisterUser:
    @staticmethod
    def random():
        username = fake.email()
        password = fake.password()
        return {"username": username, "password": password}


class ResponseModel:
    def __init__(self, status: int, response: dict = None):
        self.status = status
        self.response = response


class Item:
    def __init__(self, name, price, store_id, description, image):
        self._name = name
        self._price = price
        self._store_id = store_id
        self._description = description
        self._image = image

    @staticmethod
    def from_dict(item_dict):
        item = Item(name=item_dict['name'], price=item_dict["price"], store_id=item_dict["store_id"],
                    description=item_dict["description"], image=item_dict["image"])
        return item

    def as_dict(self):
        return {
            'price': str(self._price),
            'store_id':  self._store_id,
            'description': self._description,
            'image': self._image
        }

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def store_id(self):
        return self._store_id

    @property
    def description(self):
        return self._description

    @property
    def image(self):
        return self._image

    @name.setter
    def name(self, value):
        self._name = value
