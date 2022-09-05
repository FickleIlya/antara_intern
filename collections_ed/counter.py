from collections import Counter


def main():
    cnt = Counter(a=2, b=-3)
    print(dict(cnt))
    print(cnt)
    print(cnt.total())
    print(cnt.most_common(1))
    print(cnt.values())
    print(*cnt.elements())
    print(+cnt)
    print(-cnt)


if __name__ == "__main__":
    main()
