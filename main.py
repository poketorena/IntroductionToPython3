def main_gen(n):
    yield "start"
    yield from range(n, 0, -1)  # サブイテレータから値を作る
    yield from "abc"  # サブイテレータから値を作る
    yield from [10, 20, 30]  # サブイテレータから値を作る
    yield from sub_gen()
    yield "end"


# サブジェネレータ
def sub_gen():
    yield "X"
    yield "Y"
    yield "Z"


gen = main_gen(3)
print(list(gen))
