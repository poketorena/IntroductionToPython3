from random import randint
a = randint(0, 10)
# 判定
if 5 <= a <= 8:
    print(f"{a}:合格")
else:
    print(f"{a}:不合格")