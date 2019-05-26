from random import randint

keys = ["green", "red", "blue", "yellow"]
data = {key: randint(1, 100) for key in keys}
print(data)
