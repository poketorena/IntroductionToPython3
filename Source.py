a = {"りんご", "みかん", "桃", "いちご"}
b = {"いちご", "スイカ"}
c = ["みかん", "バナナ"]

# ここで実行時エラーが発生する！
# なぜなら | などの演算子を使った集合演算は、a, b, cなどの要素すべてがset型である必要があるから
d = a | b | c  # 和集合を求める

print(d)
