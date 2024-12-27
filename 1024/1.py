import numpy as np

# 迭代次数
iterations = 8

# 初始化x1, x2, x3的初始值为0
x1, x2, x3 = 0, 0, 0

# Jacobi迭代法
def jacobi_iter(x1, x2, x3, iterations):
    for _ in range(iterations):
        new_x1 = 10 * x2 - 2 * x3 - 8.3
        new_x2 = -10 * x1 + 2 * x3 + 7.2
        new_x3 = -(x1 + x2) / 5 + 0.84
        x1, x2, x3 = new_x1, new_x2, new_x3
        print(f"Jacobi: x1 = {x1:.4f}, x2 = {x2:.4f}, x3 = {x3:.4f}")
    return x1, x2, x3

# Gauss-Seidel迭代法
def gauss_seidel_iter(x1, x2, x3, iterations):
    for _ in range(iterations):
        x1 = 10 * x2 - 2 * x3 - 8.3
        x2 = -10 * x1 + 2 * x3 + 7.2
        x3 = -(x1 + x2) / 5 + 0.84
        print(f"Gauss-Seidel: x1 = {x1:.4f}, x2 = {x2:.4f}, x3 = {x3:.4f}")
    return x1, x2, x3

# 执行Jacobi和Gauss-Seidel迭代
print("Jacobi Iteration Results:")
jacobi_iter(x1, x2, x3, iterations)

print("\nGauss-Seidel Iteration Results:")
gauss_seidel_iter(x1, x2, x3, iterations)
