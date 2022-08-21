import datetime
import argparse
import json

from factory.factory import Factory
from services.grouping import EventGroup


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('--date_start', type=datetime.datetime.fromisoformat,
                        default=datetime.datetime.now(), help='Date of interval start')

    parser.add_argument('--date_end', type=datetime.datetime.fromisoformat,
                        default=datetime.datetime.now() + datetime.timedelta(days=30),
                        help='Date of interval end')

    parser.add_argument('--count', type=int,
                        default=5, help='Numbers of events')

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    factory = Factory(date_start=args.date_start, date_end=args.date_end)
    events = list(factory.create_events(args.count))
    print(events)
    print(json.dumps([event.to_dict() for event in events], indent=4))
    group = EventGroup.group_by_date(events)
    print(group)
