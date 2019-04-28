list_a = [1, 2, 3]
list_b = list_a
list_c = [1, 2, 3]

print(f"list_a {list_a}")
print(f"list_b {list_b}")
print(f"list_c {list_c}")

list_a[0] = 99

print()
print(f"list_a {list_a}")
print(f"list_b {list_b}")
print(f"list_c {list_c}")

list_b[1] = 100

print()
print(f"list_a {list_a}")
print(f"list_b {list_b}")
print(f"list_c {list_c}")
