import numpy as np

def estimate_eigenvalue_range(A):
    """
    Estimate the range of eigenvalues of a matrix A using Gershgorin circle theorem.
    """
    n = A.shape[0]
    lower_bound = float('inf')
    upper_bound = float('-inf')

    for i in range(n):
        row_sum = sum(abs(A[i, j]) for j in range(n) if j != i)
        center = A[i, i]
        lower_bound = min(lower_bound, center - row_sum)
        upper_bound = max(upper_bound, center + row_sum)

    return lower_bound, upper_bound

# Example matrix
A = np.array([[4, 1, 1],
              [1, 3, 1],
              [1, 1, 2]])

# Estimate Eigenvalue Range
eigenvalue_range = estimate_eigenvalue_range(A)
print("Estimated Eigenvalue Range:", eigenvalue_range)
