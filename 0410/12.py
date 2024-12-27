if __name__ == "__main__":
    print(
        ",".join(
            map(str, list(filter(lambda d: d % 2 == 1, map(int, input().split(",")))))
        )
    )
