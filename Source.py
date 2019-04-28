list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print(list_a is list_b)  # 同じオブジェクトかどうか比較する

print()
print(list_a == list_c)  # list_aとlist_cは同じ値だけど違うオブジェクト！
print(list_a is list_c)
print(list_a is not list_c)
