import numpy as np

a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
print(a)
# 偶数
print(a[a % 2 == 0])
# 奇数
print(a[a % 2 == 1])
