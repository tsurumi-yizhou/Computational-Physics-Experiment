if __name__ == "__main__":
    n = int(input())
    print(dict(zip(range(1, n + 1), map(lambda x: x * x, range(1, n + 1)))))
