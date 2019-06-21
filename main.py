import numpy as np

a = np.array([56, 45, 83, 67, 59, 41]).reshape(2, 3)
print(a)
print(a.sum())  # 全体の合計

print(a.sum(axis=0))  # 各列の合計
print(a.sum(0))  # 各列の合計

print(a.sum(axis=1))  # 各行の合計
print(a.sum(1))  # 各行の合計

print("最大値")

print(a.max())  # 全体の最大値
print(np.max(a))  # 全体の最大値

print(a.max(axis=0))  # 各列の最大値
print(a.max(0))  # 各列の最大値
print(np.max(a, axis=0))  # 各列の最大値
print(np.max(a, 0))  # 各列の最大値

print(a.max(axis=1))  # 各行の最大値
print(a.max(1))  # 各行の最大値
print(np.max(a, axis=1))  # 各行の最大値
print(np.max(a, 1))  # 各行の最大値

print("最小値")

print(a.min())  # 全体の最小値
print(np.min(a))  # 全体の最小値

print(a.min(axis=0))  # 各列の最小値
print(a.min(0))  # 各列の最小値
print(np.min(a, axis=0))  # 各列の最小値
print(np.min(a, 0))  # 各列の最小値

print(a.min(axis=1))  # 各行の最小値
print(a.min(1))  # 各行の最小値
print(np.min(a, axis=1))  # 各行の最小値
print(np.min(a, 1))  # 各行の最小値

print("平均値")

print(a.mean())  # 全体の平均値
print(np.mean(a))  # 全体の平均値

print(a.mean(axis=0))  # 各列の平均値
print(a.mean(0))  # 各列の平均値
print(np.mean(a, axis=0))  # 各列の平均値
print(np.mean(a, 0))  # 各列の平均値

print(a.mean(axis=1))  # 各行の平均値
print(a.mean(1))  # 各行の平均値
print(np.mean(a, axis=1))  # 各行の平均値
print(np.mean(a, 1))  # 各行の平均値
