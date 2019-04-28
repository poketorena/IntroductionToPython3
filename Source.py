data = [10, 21, 35, 49, 51, 60, 77, 81, 92, 100]
n = 3
data1 = data[:n]  # 最初からn-1まで
data2 = data[n:]  # nから最後まで

print(data)
print(data1)
print(data2)

data[0] = 999

# スライスの返礼地は元のリストを部分的にディープコピーしたもの？
# もとのリストを変更してもスライス後のリストに影響しない！
print()
print(data)
print(data1)
