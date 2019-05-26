import pprint
from random import random

data = {key: random() for key in "abcdefghijk"}

print(data)
print()
pprint.pprint(data)
