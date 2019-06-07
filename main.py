def hello():
    print("ハロー")


msg = hello  # 関数を代入する

print(hello)
print(msg)

msg()  # 変数msgに入っている関数を実行する
