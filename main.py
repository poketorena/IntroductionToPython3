class Simple:
    pass


Simple.greeting = lambda msg="ハロー": print(msg)

Simple.greeting("おはよう！")
Simple.greeting()
