data = {"red", "blue"}
data2 = {"blue", "yellow"}
data3 = ["blue", "green"]  # メソッドなので引数はイテラブルならOK!
data.update(data2, data3)  # 和集合で更新する
print(data)
