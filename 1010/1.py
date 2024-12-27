import numpy as np

# 给定的矩阵A和向量b
A = np.array([[1, -2, 2],
              [2, -3, -3],
              [4, 1, 6]], dtype=float)

b = np.array([-2, 4, 3], dtype=float)

# Doolittle 分解 (LU 分解)
def doolittle(A):
    n = A.shape[0]
    L = np.zeros_like(A)
    U = np.zeros_like(A)

    for i in range(n):
        # 上三角矩阵U
        for k in range(i, n):
            U[i, k] = A[i, k] - np.dot(L[i, :i], U[:i, k])

        # 下三角矩阵L
        for k in range(i, n):
            if i == k:
                L[i, i] = 1  # 对角线元素设为1
            else:
                L[k, i] = (A[k, i] - np.dot(L[k, :i], U[:i, i])) / U[i, i]

    return L, U

# 解方程L * y = b
def solve_L(L, b):
    n = L.shape[0]
    y = np.zeros_like(b)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])
    return y

# 解方程U * x = y
def solve_U(U, y):
    n = U.shape[0]
    x = np.zeros_like(y)
    for i in range(n-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

# 获取LU分解
L, U = doolittle(A)

# 解方程L * y = b
y = solve_L(L, b)

# 解方程U * x = y
x = solve_U(U, y)

print(L, U, x)
