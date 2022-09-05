from collections import deque


def tail(filename, n=10):
    "Вернуть последние 'n' строк файла"
    with open(filename) as f:
        return deque(f, n)


def main():
    dq = deque("qwe")
    cp_dq = dq.copy()
    cp_dq.append("q")
    print(cp_dq)
    print(dq)

    print(cp_dq.count("q"))

    print(cp_dq.index("q", 1))

    for row in tail("file.txt", 5):
        print(row)


if __name__ == "__main__":
    main()