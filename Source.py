a = {1, 2, 3}
b = {3, 2, 1}
c = {1, 2, 3, 4}
print(a == b)  # aとbの要素が一致しているのでTrue
print(a is b)  # 同一インスタンスでないのでFalse
print(a == c)  # cはaの要素をすべて含んでいるが同一の要素のみを持っているわけではないのでFalseになる
