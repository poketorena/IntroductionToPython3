import matplotlib.pyplot as plt
import numpy as np

x1, y1 = range(0, 5), [61, 45, 27, 88, 47]
x2, y2 = range(0, 5), [17, 39, 46, 40, 27]

labels = ["A", "B", "C", "D", "E"]
fig = plt.figure()

# 1行2列の左
ax1 = fig.add_subplot(1, 2, 1)
ax1.bar(x1, y1, color="b", tick_label=labels)
ax1.set_title("dog")
# 1行2列の右
ax2 = fig.add_subplot(1, 2, 2)
ax2.bar(x2, y2, color="g", tick_label=labels)
ax2.set_title("cat")

plt.show()
