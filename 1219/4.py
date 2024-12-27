def f(x, y):
    return 1 + (1 / x) * y
x = 1
y = 2
h = 0.25
results = [(x, y)]

while x < 2:
    k1 = f(x, y)
    k2 = f(x + h / 2, y + h * k1 / 2)
    y += h * k2
    x += h
    results.append((x, y))
    print(f"x = {x:.2f}, y = {y:.8f}")
