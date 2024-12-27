import numpy as np


def cholesky(A):
    n = A.shape[0]
    L = np.zeros_like(A)

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                L[i, j] = np.sqrt(A[i, i] - np.sum(L[i, :j] ** 2))
            else:
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
    return L


def solve(A, b):
    L = cholesky(A)
    n = len(b)
    y = np.zeros_like(b, dtype=np.float64)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    x = np.zeros_like(b, dtype=np.float64)
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(L[i + 1:, i], x[i + 1:])) / L[i, i]

    return x


A = np.array([[4, -1, 1],
              [-1, 4.25, 2.75],
              [1, 2.75, 3.5]], dtype=np.float64)
b = np.array([6, -0.5, 1.25], dtype=np.float64)

x = solve(A, b)
print("解为：", x)
