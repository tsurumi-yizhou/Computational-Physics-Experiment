from time import time
from random import uniform


def runtime(functor, arg1, arg2):
    start = time()
    functor(arg1, arg2)
    end = time()
    return end - start


def solution1(to_find, numbers):
    return sorted(numbers, key=lambda x: abs(to_find - x))[0]


def solution2(to_find, numbers):
    result = 0.0
    for i in numbers:
        if abs(i - to_find) < abs(result - to_find):
            result = i
    return result


if __name__ == "__main__":
    to_find = float(input())
    test_data = [uniform(0, 1) for _ in range(1000)]
    print("solution1: ", runtime(solution1, to_find, test_data), "s")
    print("solution2: ", runtime(solution2, to_find, test_data), "s")
