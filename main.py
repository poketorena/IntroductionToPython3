import numpy as np

a = np.array(list(range(10, 50, 10)))
b = a.reshape(2, 2)
print(a)
print(b)

print(a is b)


b[0, 0] = 99
# 同じオブジェクトでないのにbの要素の変更がaに影響してしまう！
print(b)
print(a)
