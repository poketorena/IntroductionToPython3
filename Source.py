data = {"red", "blue", "green", "yellow"}
data2 = ["blue", "black", "yellow"]  # メソッドなのでイテラブルもOK!

data.symmetric_difference_update(data2)  # 対称差集合で更新する

print(data)
