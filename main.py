import numpy as np

a = np.array(list(range(0, 100, 10)))

# 全ての要素を複製
print(a[:])

# 最初からインデックス番号3まで
print(a[:4])

# インデックス番号4から最後まで
print(a[4:])

# インデックス番号3～6
print(a[3:7])

# 先頭から1個飛び
print(a[::2])
