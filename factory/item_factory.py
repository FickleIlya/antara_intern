import random

from faker import Faker

from registration.models import Item

fake = Faker()


class ItemFactory:

    def create_item(self):
        return Item(name=fake.word(), price=str(fake.price()), store_id=random.randint(1, 1000),
                    description=fake.text(), image=fake.text())

    def create_items(self, cnt):
        for i in range(cnt):
            yield self.create_item()
