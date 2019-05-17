data = {"red", "blue", "green", "yellow"}
data2 = ["blue", "black", "yellow"]  # メソッドなので引数にイテラブルが使える

data.intersection_update(data2)  # 積集合で更新する

print(data)
