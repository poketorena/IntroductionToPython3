import numpy as np

a = np.array([56, 45, 83, 67, 59, 41]).reshape(2, 3)
print(a)
print(a.sum())  # 全体の合計

print(a.sum(axis=0))  # 各列の合計
print(a.sum(0))  # 各列の合計

print(a.sum(axis=1))  # 各行の合計
print(a.sum(1))  # 各行の合計
