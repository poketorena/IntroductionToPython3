data = {"red", "blue", "green", "yellow"}
data2 = ["blue", "black", "yellow"]  # メソッドなのでイテラブルもOK!

# 対称差集合で更新する（排他的論理和の2つの集合に対してしか適応できないという理由から引数は1つ飲み取れる）
data.symmetric_difference_update(data2)

print(data)
