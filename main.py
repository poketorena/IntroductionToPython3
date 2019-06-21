import numpy as np

a = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print(a)
b = np.array([10, 20]).reshape(2, 1)
print(b)
c = a + b
print(c)
