def menu_generator():
    yield "ワイン"
    yield "サラダ"
    yield "スープ"
    yield "ステーキ"
    yield "アイスクリーム"


menu = menu_generator()
print(type(menu))

print(next(menu))
print(next(menu))
print(next(menu))
print(next(menu))
print(next(menu))
print(next(menu))
