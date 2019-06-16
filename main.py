import matplotlib.pyplot as plt

x = [100, 200, 300, 400, 500]
y1 = [40, 65, 80, 100, 90]
y2 = [34, 56, 75, 91, 79]
y3 = [25, 47, 68, 76, 73]
y4 = [15, 40, 52, 64, 69]

plt.plot(x, y1, marker="o", color="blue", linestyle="-")
plt.plot(x, y2, marker="v", color="red", linestyle="--")
plt.plot(x, y3, marker="^", color="green", linestyle="-.")
plt.plot(x, y4, marker="d", color="m", linestyle=":")
plt.show()
