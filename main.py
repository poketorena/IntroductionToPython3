import numpy as np

a = np.array(list(range(10, 100, 10))).reshape(3, 3)

print(a)
print()
# 多次元Numpy配列のスライスは[行のスライス指定, 列のスライス指定]
# のように行と列のスライスの指定をカンマで区切って指定する！

# 0～1行目、すべての列
print(a[:2, ])
print()

# すべての行、1列目以降
print(a[:, 1:])
print()

# 1行目以降、1列目以降
print(a[1:, 1:])
