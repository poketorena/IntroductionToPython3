import numpy as np

p0 = np.array((1, 1))
p1 = np.array((6, 4))
a = p1 - p0
print(type(a))
print("a", a)

a_norm = np.linalg.norm(a)
print(a_norm)

a2 = a * 2
print("a2", a2)
a2_norm = np.linalg.norm(a2)
print(a2_norm)
