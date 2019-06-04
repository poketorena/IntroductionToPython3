fruit = {"apple": 7, "orange": 5, "mango": 3, "peach": 6}
print(type(fruit.keys()))
print(fruit.keys())
# list型のコンストラクタに渡してdict_keys型からlist型に変換する
keys1 = list(fruit.keys())
# これだとダメ
keys2 = [fruit.keys()]
print(keys1)
print(keys2)
