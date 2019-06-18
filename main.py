import numpy as np

words = np.array(["dog", "cat", "bird"])
new_words = np.insert(words, 0, "snake")
print(new_words)
