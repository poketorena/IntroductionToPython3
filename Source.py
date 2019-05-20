data = {"yellow": 3, "blue": 6, "green": 5}
print(data)
result1 = data.setdefault("blue", 10)  # "blue"キーがあるので何も変更しない
print(result1)
print(data)
result2 = data.setdefault("white", 10)  # "white"キーはないので要素を追加する
print(result2)
print(data)
