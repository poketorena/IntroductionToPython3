import copy

list_mother = [10, 20, 30, 40, 50, [11, 22, 33]]
list_work_shallow = list_mother.copy()  # リストを複製する（浅いコピー）
list_work_deep = copy.deepcopy(list_mother)  # リストを複製する（深いコピー）
list_work_slice = list_mother[:]  # リストを複製する（スライスを使う場合は浅いコピー！）
list_work_list_hikisu = list(list_mother)  # list()の引数に複製したいリストを与える場合（浅いコピー！）

print(list_mother)
print(list_work_shallow)
print(list_work_slice)
print(list_work_list_hikisu)

print()

print(list_work_shallow is list_mother)  # 値は同じだけど違うオブジェクト
print(list_work_deep is list_mother)  # 値は同じだけど違うオブジェクト
print(list_work_slice is list_mother)  # 値は同じだけど違うオブジェクト
print(list_work_list_hikisu is list_mother)  # 値は同じだけど違うオブジェクト

print()

# copy()は浅いコピー！
print(f"list_work_shallow[5] is list_mother[5] : {list_work_shallow[5] is list_mother[5]}")

# copy()は深いコピー！
print(f"list_work_deep[5] is list_mother[5] : {list_work_deep[5] is list_mother[5]}")

# スライスは浅いコピー！
print(f"list_work_slice[5] is list_mother[5] : {list_work_slice[5] is list_mother[5]}")

# list()の引数に複製したいリストを与える場合は浅いコピー！
print(f"list_work_hikisu[5] is list_mother[5] : {list_work_list_hikisu[5] is list_mother[5]}")
