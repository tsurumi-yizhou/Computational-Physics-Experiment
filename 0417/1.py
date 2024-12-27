import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from random import uniform


def f(x):
    return 1 / (1 + 4 * pow(x, 2))


def output(args):
    if args[0] != 0:
        print(args[0], end="")
    for i in range(1, len(args)):
        if args[i] > 0:
            print("+{}x^{}".format(args[i], i), end="")
        if args[i] < 0:
            print("{}x^{}".format(args[i], i), end="")


def calc(args, x):
    sum = args[0]
    for i in range(1, len(args)):
        sum += args[i] * pow(x, i)
    return sum


if __name__ == "__main__":
    x1 = np.linspace(-5, 5, 10)
    k = lagrange(x1, f(x1))

    x2 = np.linspace(-5, 5, 99)

    plt.scatter(x2, f(x2), c="red")
    plt.scatter(x2, k(x2), c="cyan")
    plt.show()

    error = np.abs(f(x2) - k(x2))
    print("误差：{}".format(error))
