import numpy as np
import matplotlib.pyplot as plt

def dydx(x, y):
    """定义微分方程 y' = y - 2x / y"""
    return y - 2 * x / y

def runge_kutta(f, x0, y0, h, x_end):
    """
    使用四阶Runge-Kutta方法求解初值问题。

    参数：
    f      - 微分方程 dy/dx = f(x, y)
    x0     - 初始值 x
    y0     - 初始值 y
    h      - 步长
    x_end  - 终止值 x

    返回：
    x_vals - x 值数组
    y_vals - y 值数组
    """
    x_vals = [x0]
    y_vals = [y0]

    x, y = x0, y0
    while x < x_end:
        # 计算 Runge-Kutta 的四个中间值
        k1 = h * f(x, y)
        k2 = h * f(x + h / 2, y + k1 / 2)
        k3 = h * f(x + h / 2, y + k2 / 2)
        k4 = h * f(x + h, y + k3)

        # 更新 x 和 y
        y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x += h

        x_vals.append(x)
        y_vals.append(y)

    return np.array(x_vals), np.array(y_vals)

# 初始条件
x0 = 0
y0 = 1
h = 0.2
x_end = 1

# 调用 Runge-Kutta 方法
x_vals, y_vals = runge_kutta(dydx, x0, y0, h, x_end)

# 打印结果
print("x values:", x_vals)
print("y values:", y_vals)

# 绘图
plt.plot(x_vals, y_vals, marker='o', label='Runge-Kutta Solution')
plt.title("Runge-Kutta Method Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()
