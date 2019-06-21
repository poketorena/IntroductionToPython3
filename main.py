import pandas as pd

df = pd.read_csv("data.csv")
header = df.columns.values
data = df.values
print(header)
print(data)
