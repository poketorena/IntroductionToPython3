data = {"red", "blue", "green", "yellow"}
data2 = ["blue", "black", "yellow"]  # メソッドなのでいてラブルもOK!

data.difference_update(data2)  # 差集合で更新する

print(data)
