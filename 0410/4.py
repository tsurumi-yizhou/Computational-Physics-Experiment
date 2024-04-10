import re

if __name__ == "__main__":
    args = re.findall("[0-9]+", input())
    print(list(args))
    print(tuple(args))
