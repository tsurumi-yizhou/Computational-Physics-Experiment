import math

# 定义f(x)和f'(x)
def f(x):
    return x**2 - 3*x - math.exp(x) + 2

def f_prime(x):
    return 2*x - 3 - math.exp(x)

# 牛顿法迭代
def newton_method(x0, tolerance=1e-8, max_iterations=100):
    x = x0
    for _ in range(max_iterations):
        fx = f(x)
        fx_prime = f_prime(x)
        x_new = x - fx / fx_prime
        if abs(x_new - x) < tolerance:
            return round(x_new, 8)  # 精确到小数后第八位
        x = x_new
    return round(x, 8)

# 初始值 x0 = 1
x0 = 1
solution = newton_method(x0)
print(solution)
