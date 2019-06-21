import numpy as np

sigma = 3.5  # 分散
mu = 65  # 平均
# 点数のサンプルデータ（正規分布の乱数で作成する）
data = sigma * np.random.randn(200) + mu  # 点数が200個入った配列
x = float(input("得点は？："))  # キーボードから得点を入力する
t_score = 10 * (x - data.mean()) / data.std() + 50  # 偏差値
print("平均点：", round(data.mean(), 1))
print("標準偏差：", round(data.std(), 1))  # 標準偏差（小数点以下第1位まで）
print("偏差値：", round(t_score, 1))
