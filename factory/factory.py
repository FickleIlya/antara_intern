import random
from datetime import datetime, timedelta

from models.event import Event, EventType
from faker import Faker

fake = Faker()

MEMBERS = ["Jerry", "Holy", "Jasmine", "Andrew", "Scott"]


class Factory:

    def __init__(self, date_start, date_end):
        self.date_start = date_start
        self.date_end = date_end

    def create_events(self, num):
        for i in range(num):
            yield self.create_event()

    def create_event(self):
        return Event(event_type=random.choice([event_type for event_type in EventType]), event_date=self.random_date(),
                     event_place=fake.word(), event_title=fake.word(), event_members=MEMBERS)

    def random_date(self):
        period = self.date_end - self.date_start
        date = datetime.combine(self.date_start,
                                datetime.min.time()) + timedelta(seconds=random.randint(0, int(period.total_seconds())))
        return date
