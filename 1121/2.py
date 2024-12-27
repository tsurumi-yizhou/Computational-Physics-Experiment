import numpy as np
import matplotlib.pyplot as plt

def improved_euler(f, x0, y0, h, x_end):
    """
    Solve the ODE y'(x) = f(x, y) using the improved Euler method.

    Parameters:
        f (function): The function f(x, y) defining the ODE.
        x0 (float): The initial value of x.
        y0 (float): The initial value of y.
        h (float): The step size.
        x_end (float): The end value of x.

    Returns:
        x_vals (numpy.ndarray): Array of x values.
        y_vals (numpy.ndarray): Array of y values.
    """
    # Initialize arrays to store results
    x_vals = np.arange(x0, x_end + h, h)
    y_vals = np.zeros_like(x_vals)

    # Set initial values
    y_vals[0] = y0

    # Iteratively apply the improved Euler method
    for i in range(len(x_vals) - 1):
        x_n, y_n = x_vals[i], y_vals[i]
        # Predict
        y_predict = y_n + h * f(x_n, y_n)
        # Correct
        y_vals[i + 1] = y_n + (h / 2) * (f(x_n, y_n) + f(x_vals[i + 1], y_predict))

    return x_vals, y_vals

# Define the ODE function f(x, y) = x^2 + y^2
def f(x, y):
    return x**2 + y**2

# Parameters
x0 = 0
y0 = 1
h = 0.05
x_end = 0.5

# Solve the ODE
x_vals, y_vals = improved_euler(f, x0, y0, h, x_end)

# Print results
for x, y in zip(x_vals, y_vals):
    print(f"x = {x:.2f}, y = {y:.6f}")

# Plot results
plt.plot(x_vals, y_vals, marker='o', label='Improved Euler')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solution of ODE using Improved Euler Method')
plt.legend()
plt.grid(True)
plt.show()
