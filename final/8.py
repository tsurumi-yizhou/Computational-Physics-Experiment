import numpy as np


def power_method(A, tolerance=1e-3):
    """
    Power Method to compute the dominant eigenvalue and corresponding eigenvector of matrix A.
    """
    n, _ = A.shape
    x = np.random.rand(n)
    x /= np.linalg.norm(x)

    while True:
        x_new = A @ x
        x_new /= np.linalg.norm(x_new)

        if np.linalg.norm(x_new - x) < tolerance:
            break

        x = x_new

    eigenvalue = x @ (A @ x) / (x @ x)
    return eigenvalue, x


A = np.array([[2, 4, 6],
              [3, 9, 15],
              [4, 16, 36]])

dominant_eigenvalue, dominant_eigenvector = power_method(A)
print("Power Method:")
print("Dominant Eigenvalue:", dominant_eigenvalue)
print("Dominant Eigenvector:", dominant_eigenvector)
