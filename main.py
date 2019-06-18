import numpy as np

a = np.array(list(range(10, 100, 10)))
b = a.reshape(3, 3)
print(a)
print(b)

print(b[0][0])
print(b[0, 0])

print(b[1][0])
print(b[1, 0])

print(b[1][1])
print(b[1, 1])

print(b[2][-1])
print(b[2, -1])
