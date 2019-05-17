a = {1, 2, 3}
b = {3, 2, 1}
c = {1, 2, 3, 4}
print(a != b)  # aとbの要素が一致しているのでFalse
print(a is b)  # 同一インスタンスでないのでFalse
print(a != c)  # aとcは違う要素を持っているのでTrue
