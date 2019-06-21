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

print(metrics.classification_report(y_test, predicted))

print(metrics.confusion_matrix(y_test, predicted))

imgs_yt_preds = list(zip(digits.images[n_train:], y_test, predicted))

for index, (image, y_t, pred) in enumerate(imgs_yt_preds[404:416]):
    plt.subplot(3, 4, index + 1)
    plt.axis("off")
    plt.tight_layout()
    plt.imshow(image, cmap="Greys", interpolation="nearest")
    plt.title(f"{y_t} pre:{pred}", fontsize=12)

plt.show()
