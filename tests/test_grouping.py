from pprint import pprint

import pytest
from datetime import datetime

from services.grouping import EventGroup
from models.event import Event
from tests.data_for_tests import *


@pytest.fixture
def events():

    events = [Event.from_dict(event) for event in EVENTS if event["type"] != "other"]
    yield events


@pytest.fixture
def events_grouped_by_date():
    events_by_date = [{datetime.fromisoformat(date).date(): events for date, events in group.items()}
                      for group in EVENTS_GROUP_BY_DATE]
    yield events_by_date


@pytest.fixture
def events_grouped_by_type():
    events_by_date = [{event_type: events for event_type, events in group.items()}
                      for group in EVENTS_GROUP_BY_TYPE]
    yield events_by_date


@pytest.mark.usefixtures("events", "events_grouped_by_date")
class TestGroup:

    def test_group_by_date(self, events, events_grouped_by_date):
        # pprint(events_grouped_by_date)
        group = EventGroup.group_by_date(events=events)
        pprint(group)
        assert group == events_grouped_by_date

    def test_group_by_type(self, events, events_grouped_by_type):
        group = EventGroup.group_by_type(events=events)
        assert group == events_grouped_by_type
