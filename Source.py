import exchange  # exchangeモジュールを読み込む

yen = 25000
rate = 114.22  # 円/ドル（中間値）
charge = 1.0  # 為替手数料
dollar = exchange.yen2dollar(yen, rate, charge)
# 四捨五入もどき
print(f"{dollar:,.2f}ドル")
# print(f"{dollar}ドル")
