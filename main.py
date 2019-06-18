import numpy as np

a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
print(a)

print(a[(a >= 5) & (a % 2 == 1)])  # 5以上の帰趨
print(a[(a % 2 == 0) | (a % 3 == 0)])  # 2または3の倍数
print(a[~(a % 3 == 0)])  # 3の倍数ではない値
