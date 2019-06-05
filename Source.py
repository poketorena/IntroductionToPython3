def route(start, end, *args):
    # 引数からルートのリストを作る
    route_list = [start]  # スタート地点
    route_list += list(args)  # 経由地点
    route_list += [end]  # ゴール地点
    # リストの要素を→で連結した文字列にする
    route_str = "→".join(route_list)
    print(route_str)


# routeを試す
start = "東京"
end = "宮崎"
# route(start, end, "神戸", "長崎", "熊本", "こなみ")
route(start, end)
