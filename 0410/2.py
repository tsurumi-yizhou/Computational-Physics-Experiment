import math

if __name__ == "__main__":
    x = list(map(str, map(math.factorial, map(int, input().split(",")))))
    print(",".join(x))
