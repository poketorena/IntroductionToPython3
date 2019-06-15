class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Player(Person):
    def __init__(self, name, age, number, position):
        super().__init__(name, age)
        self.number = number
        self.position = position


player1 = Player("青木", 16, 10, "MF")

print(player1.name)
print(player1.age)
print(player1.number)
print(player1.position)
