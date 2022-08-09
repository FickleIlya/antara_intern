import json
import random
from datetime import datetime, timedelta
from enum import Enum
from random import randrange


class PrivateEvent:
    @staticmethod
    def get_type():
        return "private"


class MeetingEvent:
    @staticmethod
    def get_type():
        return "meeting"


class CorporateEvent:
    @staticmethod
    def get_type():
        return "corporate"


class OtherEvent:
    @staticmethod
    def get_type():
        return "other"


class EventType(Enum):

    PRIVATE = PrivateEvent
    MEETING = MeetingEvent
    CORPORATE = CorporateEvent
    OTHER = OtherEvent


class EventFactory:
    def __init__(self, event_cls, date):
        self.event_type = event_cls.get_type()
        self.date = date
        self.payload = {
            "date": self.date,
            "type": self.event_type,
            "title": self.get_title(),
            "place": self.get_meet_place(),
            "participants": ["Damir", "Aleksandr", "Nikita", "Sergey", "Dmitry"]
        }

    def get_title(self):
        characters = list('abcdefghijklmnopqrstuvwxyz')
        upper_characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        numbers = list("1234567890")

        box = list()

        box += characters + upper_characters + numbers

        length = 10
        result = ''
        for i in range(5):
            for j in range(length):
                result += random.choice(box)
            result += ' '

        return result.strip()

    def get_meet_place(self):
        characters = list('abcdefghijklmnopqrstuvwxyz')
        upper_characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        numbers = list("1234567890")

        box = list()

        box += characters + upper_characters + numbers

        length = 10
        result = ''
        for j in range(length):
            result += random.choice(box)

        return result

    def to_json(self):
        if not self.payload["type"] == "other":
            return json.dumps(self.payload)


class DateRange:
    def __init__(self, start, end):
        delta = end - start
        int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
        random_second = randrange(int_delta)
        self.date = str(start + timedelta(seconds=random_second))


if __name__ == "__main__":
    for event_type in EventType:
        date_start = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
        date_end = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
        date = DateRange(date_start, date_end).date
        event = EventFactory(event_type.value(), date)
        print(event.to_json())