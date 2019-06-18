import numpy as np

a = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print(a)
b = np.append(a, [[7, 8, 9]], axis=0)
print(b)
c = np.append(a, [[7], [8]], axis=1)
print(c)
