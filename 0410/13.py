from random import uniform
import numpy as np
import matplotlib.pyplot as plt

x = np.array([uniform(0, 5) for _ in range(15)])
y = np.array([uniform(0, 5) for _ in range(15)])

plt.scatter(x, y, c=y)
plt.colorbar()
plt.title("Graph without any meaning")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
