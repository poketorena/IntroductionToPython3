keys = ["yellow", "blue", "green"]
values = [3, 6, 5]

zip_object = zip(keys, values)

data_dict = dict(zip_object)

# ここでzip_objectの2回目の評価を行っている！！！
data_list = list(zip_object)

# 普通に出力される
print(data_dict)

# zipなどで作られるイテレータは2回目以降の評価では何も返さない！！！！！
print(data_list)
