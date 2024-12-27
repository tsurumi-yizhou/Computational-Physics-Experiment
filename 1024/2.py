import numpy as np

# 系数矩阵 A 和右边的常数项 b
A = np.array([[6, 3],
              [3, 2]])

b = np.array([0, -1])

# 初始猜测 x0 = [0, 0]
x = np.array([0, 0])

# 计算初始残差 r0 = b - A * x
r = b - np.dot(A, x)

# 初始搜索方向 p0 = r0
p = r.copy()

# 设置迭代次数和容忍度
max_iter = 1000
tol = 1e-6

# 共轭梯度法迭代
for k in range(max_iter):
    # 计算 alpha_k
    Ap = np.dot(A, p)
    alpha = np.dot(r, r) / np.dot(p, Ap)

    # 更新解 x
    x = x + alpha * p

    # 更新残差 r
    r_new = r - alpha * Ap

    # 检查残差是否足够小，若足够小则停止迭代
    if np.linalg.norm(r_new) < tol:
        print(f"Converged in {k+1} iterations.")
        break

    # 计算 beta_k
    beta = np.dot(r_new, r_new) / np.dot(r, r)

    # 更新搜索方向 p
    p = r_new + beta * p

    # 更新残差 r
    r = r_new

# 输出最终的解
print("Solution:", x)
