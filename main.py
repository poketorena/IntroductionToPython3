import matplotlib.pyplot as plt
import numpy as np

labels = ["E", "D", "C", "B", "A"]
v = [17, 25, 47, 68, 91]
ex = 0, 0, 0.1, 0, 0  # パイの切り出し
plt.pie(v, explode=ex, labels=labels, autopct='%1.1f%%', startangle=90)
plt.show()
