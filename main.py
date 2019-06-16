import matplotlib.pyplot as plt
import math

x = range(0, 360)
s = [math.sin(math.radians(d)) for d in x]
c = [math.cos(math.radians(d)) for d in x]
plt.plot(x, s)
plt.plot(x, c)
plt.savefig("sin_and_cos_graph.png")
plt.show()
