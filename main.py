# クロージャの適宜
def charge(price):
    # 関数の実態
    def calc(num):
        return price * num

    return calc


# クロージャ（関数オブジェクト）を2個作る
child = charge(400)  # 子供料金400円
adult = charge(1000)  # 大人料金1000円

# 料金を計算する
price1 = child(3)  # 子供3人
price2 = adult(2)  # 大人2人

print(price1)
print(price2)
