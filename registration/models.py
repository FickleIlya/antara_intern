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
    @staticmethod
    def random_body():
        price = fake.text()
        store_id = random.randint(1, 1000)
        description = fake.text()
        image = fake.text()

        return {
            "price": str(123123),
            "store_id": store_id,
            "description": description,
            "image": image
        }

    @staticmethod
    def random_name():
        name = fake.word()
        return name
