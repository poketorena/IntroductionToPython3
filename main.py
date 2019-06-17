import matplotlib.pyplot as plt
import numpy as np

x, y = np.random.rand(100), np.random.rand(100)
v = np.random.rand(100)
plt.scatter(x, y, s=200, c=v, cmap="Blues", edgecolors="green")
plt.colorbar()
plt.grid(True)
plt.show()
