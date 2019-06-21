import numpy as np

data = np.arange(6).reshape(2, 3)
print(data)
print()

# 行を2回繰り返す
print(data.repeat(2, axis=0))
print()

# 列を2回繰り返す
print(data.repeat(2, axis=1))
