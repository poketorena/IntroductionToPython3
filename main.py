import matplotlib.pyplot as plt
import numpy as np

x1, y1 = range(0, 7), [61, 45, 27, 88, 47, 56, 61]
x2, y2 = range(0, 7), [17, 39, 46, 40, 27, 35, 41]

labels = ["A", "B", "C", "D", "E", "F", "G"]
fig = plt.figure()

# 1行2列の左
ax1 = fig.add_subplot(2, 1, 1, facecolor="cyan")
ax1.bar(x1, y1, color="b", tick_label=labels)
ax1.set_title("snake")
# 1行2列の右
ax2 = fig.add_subplot(2, 1, 2, facecolor="cyan")
ax2.bar(x2, y2, color="g", tick_label=labels)
ax2.set_title("fish")
plt.tight_layout()
plt.show()
