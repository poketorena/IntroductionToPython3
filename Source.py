a = {"earth", "wind", "fire"}
b = {"sky", "sea"}
c = {"fire", "water"}
result1 = a.isdisjoint(b)  # aとbには共通部分がないのでTrue
print(result1)
result2 = a.isdisjoint(c)  # aとcにはどちらも"fire"があるのでFalse
print(result2)
