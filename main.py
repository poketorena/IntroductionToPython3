from sklearn import datasets
import matplotlib.pyplot as plt

iris = datasets.load_iris()

print(dir(iris))

print(iris.DESCR)

x=iris.data
y=iris.target

print(x)
print(x.shape)
print(y)
print(y.shape)

print(iris.feature_names)


plt.scatter(x[:50,0],x[:50,1],color="r",marker="o",label="setosa")
plt.scatter(x[50:100,0],x[50:100,1],color="g",marker="+",label="versicolor")
plt.scatter(x[100:,0],x[100:,1],color="b",marker="x",label="virginica")

plt.title("iris Plants Database")
plt.xlabel("sepal length (cm)")
plt.ylabel("sepal width (cm)")
plt.legend()
plt.show()
