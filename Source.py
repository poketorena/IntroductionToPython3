import math

# and、filter、lambdaで不要な要素を除去したリストを作る
list_1 = [' ',' ','/','/','', '', '1', '2', '3']

print(list_1)

list_1 = list(filter(lambda x: x != ' ' and x != '/' and x != '', list_1))

print(list_1)