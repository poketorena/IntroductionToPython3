import matplotlib.pyplot as plt
import numpy as np

x1, y1 = range(0, 7), [61, 45, 27, 88, 47, 56, 61]
x2, y2 = range(0, 5), [77, 49, 56, 47, 67]
x3, y3 = range(0, 4), [56, 41, 67, 76]

labels = ["A", "B", "C", "D", "E", "F", "G"]
fig = plt.figure()

# 2行1列の上
ax1 = fig.add_subplot(2, 1, 1)
ax1.bar(x1, y1, color="b", tick_label=labels)
ax1.set_title("dog")
# 2行2列の3番（下の左）
ax2 = fig.add_subplot(2, 2, 3)
ax2.bar(x2, y2, color="g", tick_label=labels[:5])
ax2.set_title("cat")
# 2行2列の4番（下の右）
ax3 = fig.add_subplot(2, 2, 4)
ax3.bar(x3, y3, color="c", tick_label=labels[:4])
ax3.set_title("bird")
plt.tight_layout()
plt.show()
