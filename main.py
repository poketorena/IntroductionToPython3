sizelist = ["XS", "S", "M", "L"]  # この順に並び替える

# 並び替えるリスト
data = ["S", "M", "XS", "L", "M", "M", "XS", "S", "M", "L", "M"]
data.sort(key=lambda item: sizelist.index(item))
print(data)
