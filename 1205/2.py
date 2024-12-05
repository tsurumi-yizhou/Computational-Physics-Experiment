import numpy as np

def power_method(A, num_iterations=1000, tolerance=1e-10):
    """
    Power Method to compute the dominant eigenvalue and corresponding eigenvector of matrix A.
    """
    n, _ = A.shape
    x = np.random.rand(n)
    x /= np.linalg.norm(x)
    
    for _ in range(num_iterations):
        x_new = A @ x
        x_new /= np.linalg.norm(x_new)

        # Check for convergence
        if np.linalg.norm(x_new - x) < tolerance:
            break

        x = x_new

    eigenvalue = x @ (A @ x) / (x @ x)
    return eigenvalue, x

# Example matrix
A = np.array([[4, 1, 1],
              [1, 3, 1],
              [1, 1, 2]])

# Power Method
dominant_eigenvalue, dominant_eigenvector = power_method(A)
print("Power Method:")
print("Dominant Eigenvalue:", dominant_eigenvalue)
print("Dominant Eigenvector:", dominant_eigenvector)
