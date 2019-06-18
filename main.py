import numpy as np

a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
print(a)

b = a.reshape(4, 4)
print(b)
print(b[b > 5])
