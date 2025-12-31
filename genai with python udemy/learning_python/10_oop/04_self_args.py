class ChaiCup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"

cup = ChaiCup()
print(cup.describe())
# print(ChaiCup.describe(cup))

cup_two = ChaiCup()
cup_two.size = 100

print(cup_two.describe())