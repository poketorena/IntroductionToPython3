class Simple:
    pass


def hello(msg="ハロー"):
    print(msg)


Simple.greeting = hello

Simple.greeting("おはよう！")
Simple.greeting()
