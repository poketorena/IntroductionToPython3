data = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
print(data)
result = [num * 2 for alist in data for num in alist]
print(result)
