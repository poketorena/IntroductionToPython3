class Simple:
    pass


obj1 = Simple()
obj2 = Simple()


def drum(beat="トコトコ"):
    print(beat)


def sax(phrase="ブーブー"):
    print(phrase)


obj1.play = drum
obj2.play = sax

# 追加したメンバーを削除
obj1.play = None
del obj2.play

# 削除したので呼び出すことはできない！
obj1.play()
obj2.play()
