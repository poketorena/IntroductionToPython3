import numpy as np

a = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
b = np.array([1, 2, 9, 4, 8, 6]).reshape(2, 3)

print(a)
print(b)

c = (a == b)
print(c)

# 行列A、Bを比較して要素が同じ数、要素が異なる数を数える
print(np.sum(a == b))
print(np.sum(a != b))
