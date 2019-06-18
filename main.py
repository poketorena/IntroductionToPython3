import numpy as np

words = np.array(["dog", "cat", "bird"])
new_words = np.delete(words, len(words) - 1)
print(new_words)
