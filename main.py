from sklearn import datasets
from sklearn import svm
from sklearn import metrics
import matplotlib.pyplot as plt

digits = datasets.load_digits()

n_train = len(digits.data) * 2 // 3  # データの2/3の個数

x_train = digits.data[:n_train]  # dataの前半2/3
y_train = digits.target[:n_train]  # targetの前半2/3

x_test = digits.data[n_train:]  # dataの後半1/3
y_test = digits.target[n_train:]  # targetの後半1/3

print([d.shape for d in [x_train, y_train, x_test, y_test]])

clf = svm.SVC(gamma=0.001)  # 学習機
clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))

predicted = clf.predict(x_test)
print((y_test != predicted).sum())

miss_list = y_test != predicted

# 学習結果のレポート
print(metrics.classification_report(y_test, predicted))

# 数字ごとに正解数と読み間違えた数字を調べる（混同行列）
print(metrics.confusion_matrix(y_test, predicted))

# 誤認識のみに絞り込む
imgs_yt_preds = [value for value in list(zip(digits.images[n_train:], y_test, predicted)) if value[1] != value[2]]

# 画像イメージと分類結果（404～415の12文字を表示）
for index, (image, y_t, pred) in enumerate(imgs_yt_preds):
    plt.subplot(7, 4, index + 1)
    plt.axis("off")
    plt.tight_layout()
    plt.imshow(image, cmap="Greys", interpolation="nearest")
    plt.title(f"{y_t} pre:{pred}", fontsize=12)

plt.show()
