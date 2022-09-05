from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


def named_tuple_test(values: list) -> tuple:
    NamedTuple = namedtuple("NamedTuple", ["key1", "key2", "key3"])
    nt = NamedTuple(values[0], values[1], values[2])
    return nt


def dict_to_namedtuple(d: dict) -> tuple:
    NamedTuple = namedtuple("NamedTuple", [key for key in d])
    nt = NamedTuple(**d)
    return nt


def main():
    values = [1, 2, "hello"]
    named_tuple = named_tuple_test(values)
    print(named_tuple)

    point = Point(1, 2)
    # keys in namedtuple are checked for isidentifier, so instance of class, int, "int" do not work

    test_dict = {
        "key1": 1,
        "key2": 2,
        "key3": 3
    }
    named_tuple = dict_to_namedtuple(test_dict)
    print(named_tuple.key2)


if __name__ == "__main__":
    main()
