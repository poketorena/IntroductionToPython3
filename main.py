from sklearn import datasets, linear_model
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt

boston = datasets.load_boston()

print(dir(boston))

print(boston.DESCR)

boston_df = DataFrame(boston.data)  # DataFrame型にする
boston_df.columns = boston.feature_names  # 列名を指定する（列名を名前で取り出せるようになる）
boston_df["Price"] = boston.target  # 住宅価格を追加する
print(boston_df[:5])

rooms_train = DataFrame(boston_df["RM"])  # 部屋数のデータを抜き出す
y_train = boston.target
model = linear_model.LinearRegression()  # 回帰モデルを作る
model.fit(rooms_train, y_train)  # 訓練する

# 部屋数のテストデータを作る
tmp_min = rooms_train.values.flatten().min()
tmp_max = rooms_train.values.flatten().max()

rooms_test = DataFrame(np.arange(tmp_min, tmp_max, 0.1, dtype=np.float64))
prices_test = model.predict(rooms_test)  # モデルを使って住宅価格を予想する

plt.scatter(rooms_train.values.ravel(), y_train, c="b", alpha=0.5)  # 訓練データ
plt.plot(rooms_test.values.ravel(), prices_test, c="r")  # 回帰直線
plt.title("Boston House Prices dataset")
plt.xlabel("rooms")
plt.ylabel("price $1000's")  # y軸のラベル
plt.show()
