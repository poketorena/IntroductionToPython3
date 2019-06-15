def num_generator():
    n = 0
    while True:
        num = n * n + 2 * n + 3
        yield num
        n += 1


# 何かを扱う関数
def do_something(num):
    return (num % 2, num % 3)


# ジェネレータが返す値を使って処理を行う
gen = num_generator()
for i in range(1, 10):
    num = next(gen)
    result = do_something(num)
    print(result)
