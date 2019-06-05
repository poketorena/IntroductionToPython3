import os

print(os.getcwd())  # カレントディレクトリを確認する

os.chdir("./hoge")  # 現在のディレクトリにあるhogeフォルダに移動する

print(os.getcwd())  # カレントディレクトリを確認する
