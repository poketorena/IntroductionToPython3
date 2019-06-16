import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
x_pos = range(0, 10)
v = [91, 45, 17, 88, 47, 87, 49, 56, 67, 77]
plt.bar(x_pos, v)
# plt.bar(x_pos, v, tick_label=labels)
plt.show()
