from functools import partial


def main():
    base_eight = partial(int, base=8)
    print(base_eight('0o177'))

    base_sixteen = partial(int, base=16)
    print(base_sixteen("0xf"))


if __name__ == "__main__":
    main()

