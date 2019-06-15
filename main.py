from goods_property import Goods

shoes = Goods("dream", 6800)
print(shoes.name)
shoes.name = "Dream 8"
print(shoes.name)
print(shoes.price)

shoes2 = Goods("sky", 10000)
print(shoes2.name)
shoes2.name = "Sky 8"
print(shoes2.name)
print(shoes2.price)

shoes.price = 7200
