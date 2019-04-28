list_mother = [10, 20, 30, 40, 50]
list_work = list_mother.copy()  # リストを複製する（浅いコピー）
print(list_mother)
print(list_work)
print(list_work is list_mother)  # 値は同じだけど別のオブジェクト

list_work[0] = 99

print()
print(list_mother)
print(list_work)
