class Simple:
    pass


obj = Simple()
obj.a = 123
print(obj.a)

Simple.hello = lambda _: print("Hello!")

obj.hello()
