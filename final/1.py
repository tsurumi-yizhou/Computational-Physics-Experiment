import math

def f(x):
    return math.sqrt(1 + x**2)

def g(x):
    return x * math.sqrt(1 + x**2)

def integral(f, up, down, step=0.000001):
    i = up
    sum = 0
    while i <= down:
        sum += f(i) * step
        i += step
    return sum

a1 = 6 * (2 * integral(g, 0, 1) - integral(f, 0, 1))
a0 = integral(f, 0, 1) - 0.5 * a1
print(a0, a1)