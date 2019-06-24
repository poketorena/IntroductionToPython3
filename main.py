from sklearn import datasets
from pandas import DataFrame

boston = datasets.load_boston()

print(dir(boston))

print(boston.DESCR)

boston_df = DataFrame(boston.data)  # DataFrame型にする
boston_df.columns = boston.feature_names  # 列名を指定する（列名を名前で取り出せるようになる）
boston_df["Price"] = boston.target  # 住宅価格を追加する
print(boston_df[:5])
