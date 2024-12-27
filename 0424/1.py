import numpy as np
import matplotlib.pyplot as plt

# 示例数据
x = np.array([1, 2, 3, 4, 5])
y = np.array([1.2, 1.9, 3.0, 3.8, 5.1])

# 一次多项式拟合
coeff_linear = np.polyfit(x, y, 1)  # [a1, b1]
y_linear_fit = np.polyval(coeff_linear, x)

# 二次多项式拟合
coeff_quadratic = np.polyfit(x, y, 2)  # [a2, b2, c2]
y_quadratic_fit = np.polyval(coeff_quadratic, x)

# 作图
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', label='Original Data', zorder=5)
plt.plot(x, y_linear_fit, color='red', label=f'Linear Fit: y = {coeff_linear[0]:.2f}x + {coeff_linear[1]:.2f}', linestyle='--')
plt.plot(x, y_quadratic_fit, color='green', label=f'Quadratic Fit: y = {coeff_quadratic[0]:.2f}x^2 + {coeff_quadratic[1]:.2f}x + {coeff_quadratic[2]:.2f}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Fitting: Linear and Quadratic')
plt.legend()
plt.grid(True)
plt.show()
