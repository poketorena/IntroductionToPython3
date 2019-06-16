import matplotlib.pyplot as plt
import numpy as np

x1 = np.random.rand(100)
y1 = np.random.rand(100)

x2 = np.random.rand(100)
y2 = np.random.rand(100)

plt.scatter(x1, y1, marker="+", color="green")
plt.scatter(x2, y2, marker="^", color="red")
plt.show()
