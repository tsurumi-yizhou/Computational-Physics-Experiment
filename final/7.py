def newton(f, df, x0, tolerance=1e-4):
    x = x0
    for i in range(10000):
        fx = f(x)
        dfx = df(x)
        new = x - fx / dfx
        if abs(new - x) < tolerance:
            return round(new, 4)
        x = new
    return round(x, 4)

f = lambda x: x**3 + 4 * x**2 - 10
df = lambda x: 3 * x**2 + 8 * x
print(newton(f=f, df=df, x0=1.5))