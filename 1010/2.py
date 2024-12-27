import numpy as np

# 给定的矩阵A和向量b
A = np.array([[0.02, 61.3],
              [3.43, -8.5]])
b = np.array([61.5, 25.8])

# LU分解并进行列主元选择
def lu_decompose(A):
    n = len(A)
    L = np.zeros_like(A)
    U = np.copy(A)
    P = np.eye(n)

    for i in range(n):
        # 列主元选择
        max_row = np.argmax(np.abs(U[i:n, i])) + i
        if i != max_row:
            U[[i, max_row], :] = U[[max_row, i], :]
            P[[i, max_row], :] = P[[max_row, i], :]
            L[[i, max_row], :] = L[[max_row, i], :]

        for j in range(i + 1, n):
            L[j, i] = U[j, i] / U[i, i]
            U[j, i:] -= L[j, i] * U[i, i:]
    np.fill_diagonal(L, 1)
    return L, U, P

# 解Ax = b的方程组
def solve_lu(L, U, P, b):
    # 前代解Ly = Pb
    Pb = np.dot(P, b)
    y = np.zeros_like(b)
    for i in range(len(L)):
        y[i] = Pb[i] - np.dot(L[i, :i], y[:i])

    # 回代解Ux = y
    x = np.zeros_like(b)
    for i in range(len(U)-1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

# LU分解
L, U, P = lu_decompose(A)

# 求解方程
x = solve_lu(L, U, P, b)

print(x)
