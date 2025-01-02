import numpy as np

def sor_iteration(A, b, omega=0.9, tolerance=1e-4):
    n = len(b)
    x = np.zeros_like(b, dtype=float)
    while True:
        new = np.copy(x)
        for i in range(n):
            s1 = sum(A[i, j] * new[j] for j in range(i))
            s2 = sum(A[i, j] * x[j] for j in range(i + 1, n))
            new[i] = (1 - omega) * x[i] + omega * (b[i] - s1 - s2) / A[i, i]
        if np.linalg.norm(new - x, ord=np.inf) < tolerance:
            return new
        x = new

A = np.array([
    [5, 2, 1],
    [-1, 4, 2],
    [2, -3, 10]
])
b = np.array([-12, 20, 3])
print(sor_iteration(A, b))