import numpy as np

a = np.array([2.1, 3.8, 2.5, 4.3, 5.1, 1.6]).reshape(3, 2)

print(a)

a2 = a[:2, ].astype(int)
print(a2)
