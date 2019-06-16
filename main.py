import matplotlib.pyplot as plt

x = [100, 200, 300, 400, 500]
y1 = [40, 65, 80, 100, 90]
y2 = [34, 56, 75, 91, 79]
y3 = [25, 47, 68, 76, 73]
y4 = [15, 40, 52, 64, 69]

plt.plot(x, y1, marker="o", color="blue", linestyle="-", label="Y1")
plt.plot(x, y2, marker="v", color="red", linestyle="--", label="Y2")
plt.plot(x, y3, marker="^", color="green", linestyle="-.", label="Y3")
plt.plot(x, y4, marker="d", color="m", linestyle=":", label="Y4")
plt.legend(loc="upper left")  # 凡例を作る（位置は左上）
plt.show()
