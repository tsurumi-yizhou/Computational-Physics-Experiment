import numpy as np
from scipy.integrate import quad

# 定义被积函数
def f(x):
    return x**2 + np.sin(x)

# 复化梯形公式实现
def trapezoidal_rule(func, a, b, n):
    x = np.linspace(a, b, n+1)
    y = func(x)
    h = (b - a) / n
    integral = h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])
    return integral

# 积分上下限
a, b = -2, 2

# 精确积分值（通过高精度数值积分求得）
true_value, _ = quad(f, a, b)

# 分区数
subdivisions = [40, 80, 200]

# 计算不同分区数下的结果
results = {
    "Subdivisions": [],
    "Approximation": [],
    "Error": [],
}

for n in subdivisions:
    approx = trapezoidal_rule(f, a, b, n)
    error = abs(approx - true_value)
    results["Subdivisions"].append(n)
    results["Approximation"].append(approx)
    results["Error"].append(error)

# 输出结果
for i in range(len(subdivisions)):
    print(f"分区数: {results['Subdivisions'][i]}, 近似值: {results['Approximation'][i]:.10f}, 误差: {results['Error'][i]:.10f}")
