from datetime import datetime
from enum import Enum


class EventType(Enum):
    PRIVATE = "private"
    MEETING = "meeting"
    Corporate = "corporate"
    OTHER = "other"


class Event:

    def __init__(self, event_type: EventType, event_title: str, event_date: datetime, event_members: list,
                 event_place: str):

        self._event_type = event_type
        self._event_title = event_title
        self._event_date = event_date
        self._event_members = event_members
        self._event_place = event_place

    def to_dict(self):
        return {
            'type': self._event_type.value,
            'date': self._event_date.isoformat(),
            'title': self._event_title,
            'members': self._event_members,
            'place': self._event_place,
        }

    @staticmethod
    def from_dict(data):
        return Event(event_type=EventType(data["type"]), event_title=data["title"],
                     event_date=datetime.fromisoformat(data["date"]), event_members=data["members"],
                     event_place=data["place"])

    @property
    def event_type(self):
        return self._event_type

    @property
    def event_title(self):
        return self._event_title

    @property
    def event_date(self):
        return self._event_date

    @property
    def event_members(self):
        return self._event_members

    @property
    def event_place(self):
        return self._event_place
