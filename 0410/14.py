import numpy as np

m = np.matrix([list(map(lambda j: (i + j) % 2, range(19))) for i in range(19)])
