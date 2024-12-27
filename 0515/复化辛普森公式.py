import numpy as np

# Function to integrate
def f(x):
    return x**2 + np.sin(x)

# Composite Simpson's Rule
def composite_simpson(a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    y = f(x)
    integral = y[0] + y[-1] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2])
    return (h / 3) * integral

# Exact integral for comparison
exact_integral = 4**3 / 3 + np.cos(-2) - np.cos(2)

# Calculate for different intervals
intervals = [40, 80, 200]
results = {n: composite_simpson(-2, 2, n) for n in intervals}

# Calculate errors
errors = {n: abs(results[n] - exact_integral) for n in intervals}

print(results)
