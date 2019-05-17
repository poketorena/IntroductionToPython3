data = {"red", "blue"}
data2 = {"blue", "yellow"}
data3 = {"blue", "green"}

data |= data2  # 和集合で置き換える
data |= data3  # 和集合で置き換える

print(data)
