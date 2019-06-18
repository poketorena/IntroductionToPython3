import matplotlib.pyplot as plt
import numpy as np

x1, y1 = range(0, 5), [61, 45, 27, 88, 47]
x2, y2 = range(0, 5), [17, 39, 46, 40, 27]

labels = ["A", "B", "C", "D", "E"]
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True)

ax1.bar(x1, y1, color="b", tick_label=labels)
ax1.set_title("dog")
ax2.bar(x2, y2, color="g", tick_label=labels)
ax2.set_title("cat")
plt.show()
