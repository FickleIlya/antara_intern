from itertools import groupby
from enum import Enum

things = [("animal", "bear"), ("animal", "duck"), ("plant", "cactus"), ("vehicle", "speed boat"),
          ("vehicle", "school bus")]

for key, group in groupby(things, lambda x: x[0]):
    # print([i for i in group])
    for thing in group:
        # print(key)
        print("A %s is a %s." % (thing[1], key))
    print("")


class EnumTest(Enum):
    OTHER = "other"
    ANOTHER = "another"


print(EnumTest("other").value)
