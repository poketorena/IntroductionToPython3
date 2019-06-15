class A:  # Aクラス
    def hello(self):
        print("ハロー")


class B(A):
    def bye(self):
        print("グッバイ")


obj = B()
obj.hello()
obj.bye()
