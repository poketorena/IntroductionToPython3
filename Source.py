a = {"blue", "red"}
b = {"blue", "green", "red", "pink", "white"}
c = ["blue", "green", "red", "pink", "white"]
print(a.issubset(b))
print(a.issubset(c))  # メソッドは引数にイテラブルを取れる！
print(a <= b)
# print(a <= c)
