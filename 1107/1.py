# 定义迭代函数
def iterate(x0, tolerance=1e-5, max_iter=100):
    x_k = x0
    for k in range(max_iter):
        x_next = 1 + 1 / (2 * x_k)  # 迭代公式
        if abs(x_next - x_k) < tolerance:  # 满足精度要求
            return x_next
        x_k = x_next
    return x_k

# 初始值 x0 = 1.5
initial_value = 1.5
root = iterate(initial_value)

print(f"The root near 1.5 is approximately: {root}")
