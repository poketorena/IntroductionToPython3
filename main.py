import numpy as np

f = np.array([8.66, 5.0])
s = np.array([20, 0])

f = np.linalg.norm(f)
s = np.linalg.norm(s)
rad = np.radians(30)  # 30度をラジアンに換算
w = f * s * np.cos(rad)
print(w)
