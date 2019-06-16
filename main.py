import matplotlib.pyplot as plt
import numpy as np

x, y = np.random.rand(100), np.random.rand(100)
v = np.random.rand(100) * 1000 + 50
plt.scatter(x, y, marker="o", s=v, color="lightgreen", alpha=0.5, linewidths=2, edgecolors="green")
plt.show()
