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

obj1.play()
obj2.play()
