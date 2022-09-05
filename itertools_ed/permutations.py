from itertools import permutations


def main():
    string = "ABC"
    unique_combines = permutations(string, 2)

    for combine in unique_combines:
        print(combine)


if __name__ == "__main__":
    main()
