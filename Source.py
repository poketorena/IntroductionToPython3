a = {1999, 2011, 2013, 2014, 2016, 2017}
b = {2011, 2013, 2014}
c = [2011, 2013, 2014]
print(a.issuperset(b))
print(a.issuperset(c))  # メソッドは引数にイテラブルを取れる！
print(a >= b)
# print(a <= c)
