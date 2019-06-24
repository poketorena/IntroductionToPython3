from sklearn import datasets
from sklearn import linear_model
from sklearn.model_selection import ShuffleSplit

iris = datasets.load_iris()  # アヤメのデータセットを読み込む

x = iris.data  # データ
y = iris.target  # ターゲット

ss = ShuffleSplit(train_size=0.6, test_size=0.4, random_state=0)

train_index, test_index = next(ss.split(x))  # 分割するインデックス番号
x_train, y_train = x[train_index], y[train_index]  # 訓練データ
x_test, y_test = x[test_index], y[test_index]  # テストデータ

clf = linear_model.LogisticRegression()  # 学習機のアルゴリズムを変えてみる
clf.fit(x_train, y_train)  # 学習する

print(clf.score(x_test, y_test))
