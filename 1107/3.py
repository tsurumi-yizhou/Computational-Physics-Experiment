import numpy as np

def newton_method(f, J, x0, tol=5e-5, max_iter=100):
    """
    Newton's method for solving a system of nonlinear equations.

    Parameters:
        f (function): A function that returns the system of equations.
        J (function): A function that returns the Jacobian matrix of the system.
        x0 (numpy array): Initial guess.
        tol (float): Tolerance for convergence.
        max_iter (int): Maximum number of iterations.

    Returns:
        numpy array: Solution vector.
    """
    x = x0
    for i in range(max_iter):
        F = f(x)
        J_inv = np.linalg.inv(J(x))  # Inverse of the Jacobian
        dx = -J_inv @ F
        x = x + dx

        if np.linalg.norm(dx) < tol:
            print(f"Converged in {i + 1} iterations.")
            return x

    raise ValueError("Newton's method did not converge within the maximum number of iterations.")

def equations(x):
    """Define the system of equations."""
    return np.array([
        x[0]**2 + x[1]**2 - 4,
        x[0]**2 - x[1]**2 - 1
    ])

def jacobian(x):
    """Define the Jacobian matrix of the system."""
    return np.array([
        [2 * x[0], 2 * x[1]],
        [2 * x[0], -2 * x[1]]
    ])

# Initial guess
x0 = np.array([1.6, 1.2])

# Solve using Newton's method
solution = newton_method(equations, jacobian, x0)

print("Solution:", solution)
