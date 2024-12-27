def newtondownhill(f, fp, x0, tol=1e-8, max=100):
    x = x0
    for i in range(max):
        fx = f(x)
        fpx = fp(x)
        delta = -fx / fpx
        new_x = x + delta
        while abs(f(new_x)) > abs(fx):
            delta /= 2
            new_x = x + delta
        x = new_x
        if abs(fx) < tol:
            return x

def f(x):
    return x ** 3 - x - 1

def fp(x):
    return 3 * x ** 2 - 1

x0 = 1.5

root = newtondownhill(f, fp, x0)

print(f"x = {root:.8f}")

