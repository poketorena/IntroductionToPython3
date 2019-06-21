import numpy as np

a = np.array([1, 2, 0])
b = np.array([0, 1, -1])
c = np.cross(a, b)  # 外積（右手系（右手の親指a、人差し指b、中指c））
print(c)
