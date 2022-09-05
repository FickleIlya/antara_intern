from itertools import chain


def main():

    # chain
    lst = ['foo', range(10), ['one', 'two']]
    chain_iter = chain(lst, range(5))
    # # print(chain_iter)
    for i in chain_iter:
        print(i)

    print()
    range1 = range(5, 10)
    range2 = range(1, 5)

    # chain(range1, range2) != range1 + range2
    for i in chain(range1, range2):
        print(i)

    # chain.from_iterable()
    print(list(chain.from_iterable(lst)))


if __name__ == "__main__":
    main()
