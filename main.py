from sklearn import datasets
digits=datasets.load_digits()

print(dir(digits))

print(digits.DESCR)

print(digits.data.shape)
print(digits.data)
print(digits.target.shape)
print(digits.target)
