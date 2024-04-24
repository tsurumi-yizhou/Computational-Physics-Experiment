import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange, interp1d, CubicSpline


def work(x, y, method):
    y_res = method(x, y)
    x_dis = np.linspace(0, 1, 100)
    plt.scatter(x_dis, y_res(x_dis), c="cyan")
    plt.scatter(x, y, c="red")
    plt.show()


def read(file):
    x = []
    y = []
    line = file.readline()
    if line.startswith("direction"):
        line = file.readline()
    while line:
        if line.startswith("direction"):
            break
        a, b = map(float, line.split())
        x.append(a)
        y.append(b)
        line = file.readline()
    return x, y


if __name__ == "__main__":
    with open("data") as file:
        for _ in range(3):
            data = read(file)
            x, y = data
            work(x, y, lagrange)
            work(x, y, CubicSpline)
