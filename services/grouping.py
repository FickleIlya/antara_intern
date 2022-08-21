from datetime import datetime
from itertools import groupby


class EventGroup:
    @staticmethod
    def group_by_date(events):
        result = [{
            date: [event.to_dict() for event in group if event.event_type.value != "other"]} for date, group
            in groupby(sorted(events,
                              key=lambda event: event.event_date), lambda event: event.event_date.date())
        ]
        return result

    @staticmethod
    def group_by_type(events):
        result = [{
            event_type: [event.to_dict() for event in group]} for event_type, group in
            groupby(sorted(events, key=lambda event: event.event_type.value), lambda event: event.event_type.value)
            if event_type != "other"
        ]
        return result
