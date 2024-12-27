from random import uniform

if __name__ == "__main__":
    numbers = [uniform(0, 1) for _ in range(1000)]
    x = float(input())
    print(sorted(numbers, key=lambda v: abs(v - x))[0])
