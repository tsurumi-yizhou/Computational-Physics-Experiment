import numpy as np
import matplotlib.pyplot as plt

# 定义微分方程的右侧函数 f(x, y)
def f(x):
    return np.cos(2 * x) + np.sin(3 * x)

# 显示Euler方法求解
def euler_method(h, x_range, y0):
    x_values = np.arange(x_range[0], x_range[1] + h, h)  # 离散的 x 值
    y_values = np.zeros(len(x_values))                  # 初始化 y 值
    y_values[0] = y0                                    # 设置初始值

    for i in range(1, len(x_values)):
        y_values[i] = y_values[i - 1] + h * f(x_values[i - 1])

    return x_values, y_values

# 参数设置
h = 0.25
x_range = [0, 1]
y0 = 1

# 求解并绘图
x_values, y_values = euler_method(h, x_range, y0)

# 输出结果
for xi, yi in zip(x_values, y_values):
    print(f"x = {xi:.2f}, y = {yi:.6f}")

# 绘制结果
plt.plot(x_values, y_values, 'o-', label="Euler Approximation")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Euler Method for ODE")
plt.legend()
plt.grid()
plt.show()
