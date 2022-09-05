from itertools import product


def main():
    x = ['a', 'b', 'c']
    y = ['1', '2']
    z = ["A", "B", "C"]
    print(list(product(x, y, z)))

    print(list(product(y, repeat=1)))


if __name__ == "__main__":
    main()
