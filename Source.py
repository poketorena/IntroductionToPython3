a = (1, 2, 3)
b = a
c = (1, 2, 3)

print(a == b)
print(a is b)
print(a == c)
print(a is c)  # Falseのはずだけど同じidが割り当てられることもある？？？

print(id(a))
print(id(b))
print(id(c))
