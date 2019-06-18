import numpy as np

a = np.arange(10, 70, 10).reshape(2, 3)

print(a)

for i, item in np.ndenumerate(a):
    # iには(行, 列)のタプルが入る
    print(i, item)
