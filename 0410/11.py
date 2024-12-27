if __name__ == "__main__":
    print(
        ",".join(
            map(
                lambda d: f"{d:b}",
                list(
                    filter(
                        lambda x: x % 5 == 0,
                        list(map(lambda word: int(word, 2), input().split(","))),
                    )
                ),
            )
        )
    )
