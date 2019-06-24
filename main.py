from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()

print(dir(iris))

print(iris.DESCR)

x = iris.data
y = iris.target

print(x)
print(x.shape)
print(y)
print(y.shape)

print(iris.feature_names)

for i, cl, mk, lb in zip([0, 1, 2], "rgb", "o+x", iris.target_names):
    plt.scatter(x[y == i][:, 0], x[y == i][:, 1], color=cl, marker=mk, label=lb)

plt.title("iris Plants Database")
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.legend()
plt.show()
