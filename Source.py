def calc(num):
    unit_price = 180  # 単価
    try:
        num = float(num)  # 数値に変換する
        return num * unit_price
    except:
        return None  # 変換がエラーになったらNoneを返す

result = calc(2)

print(result)
