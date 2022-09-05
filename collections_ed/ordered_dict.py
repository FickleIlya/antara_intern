from collections import OrderedDict


def main():
    od = OrderedDict([(1, "first"), (2, "second")])
    for k, v in od.items():
        print(f"{k}: {v}")

    od.move_to_end(2, last=False)
    print(od)

    print(list(od.items()))

    od.popitem(last=True)
    print(od)


if __name__ == "__main__":
    main()
