from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()

print(digits.data[0])
print(digits.images[0])

plt.matshow(digits.images[0], cmap="Greys")
plt.show()

print(digits.target[0])
