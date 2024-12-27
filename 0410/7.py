if __name__ == "__main__":
    a, b = map(int, input().split(","))
    print([list(map(lambda x: i * x, range(b))) for i in range(a)])
