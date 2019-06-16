import matplotlib.pyplot as plt

labels = ["Green", "Red", "Yellow", "Blue", "Black", "White"]
x_pos = range(0, 6)
a = [34, 46, 54, 45, 56, 37]
b = [17, 47, 55, 67, 38, 49]
bar1 = plt.bar(x_pos, a, color="g")
bar2 = plt.bar(x_pos, b, color="c", bottom=a)
plt.xticks(x_pos, labels, rotation="vertical")
plt.legend((bar1, bar2), ("man", "woman"), loc="upper right")
plt.show()
