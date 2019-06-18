import numpy as np

a = np.array([0, 1, 2])
print(a)
b = np.insert(a, 1, 77)
print(b)
b = np.insert(b, 1, [88, 99])
print(b)
