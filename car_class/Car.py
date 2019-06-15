class Car:
    # クラス変数
    maker = "PEACE"  # 自動車メーカー
    count = 0  # 台数

    # クラスメソッド
    @classmethod
    def countup(cls):
        cls.count += 1
        print(f"出荷台数：{cls.count}")

    def __init__(self, color="white"):
        Car.countup()  # カウントアップする
        self.mynumber = Car.count  # 自分の番号（何台目に作られたか）
        self.color = color
        self.mileage = 0

    def drive(self, km):
        self.mileage += km
        msg = f"{km}kmドライブしました。総距離は{self.mileage}kmです。"
        print(msg)
