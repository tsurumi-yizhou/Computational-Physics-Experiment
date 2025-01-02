from scipy.interpolate import CubicSpline

x = [-1, 0, 1]
y = [2, 0, 2]

print(CubicSpline(x, y).c)