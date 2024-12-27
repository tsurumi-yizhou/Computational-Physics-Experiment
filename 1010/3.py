import numpy as np

# 定义三对角矩阵的系数和常数向量
a = np.array([1, 1, 1])  # 下对角线
b = np.array([2, 3, 1, 1])  # 主对角线
c = np.array([1, 1, 2])  # 上对角线
d = np.array([1, 2, 2, 0])  # 常数向量

n = len(d)

# 前向消元
for i in range(1, n):
    m = a[i-1] / b[i-1]
    b[i] -= m * c[i-1]
    d[i] -= m * d[i-1]

# 回代求解
x = np.zeros(n)
x[-1] = d[-1] / b[-1]

for i in range(n-2, -1, -1):
    x[i] = (d[i] - c[i] * x[i+1]) / b[i]

print("解为：", x)
