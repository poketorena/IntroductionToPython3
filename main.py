import numpy as np

a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
a = a.reshape(4, 4)
print(a)
print()

a[a % 2 == 0] = 0  # 偶数を0に置き換える
print(a)
print()

a[a % 2 == 1] = 1  # 奇数を1に置き換える
print(a)
print()
