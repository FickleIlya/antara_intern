from functools import lru_cache


@lru_cache(maxsize=128)
def factorial(n):
    return n * factorial(n-1) if n else 1


def main():
    print(factorial(10))

    print(factorial(2))

    print(factorial(12))


if __name__ == "__main__":
    main()
