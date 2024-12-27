import numpy as np

a, b, c = 1, 0, -3
delta = b ** 2 - 4 * a * c
x1 = (-b + np.sqrt(delta)) / (2 * a)
x2 = (-b - np.sqrt(delta)) / (2 * a)

print(f"x1={x1:.8f},x2={x2:.8f}")
