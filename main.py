import numpy as np

a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
print(a)

# クラスメソッドだと要素をソートした新しいNumpy配列を返す
a_descend = np.sort(a)[::-1]

print("a", a)
print("a_descend", a_descend)
