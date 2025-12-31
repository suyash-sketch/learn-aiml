class Chai:
    temperature = "hot"
    strength = "strong"

cutting = Chai()

print(cutting.temperature)

cutting.temperature = "mild"
cutting.cup = "small"
print("Cup size:",cutting.cup)
print("After changing:",cutting.temperature)
print("Direct look into the class:",Chai.temperature)

cutting.temperature = "cold"
del cutting.temperature
del cutting.cup
print(cutting.temperature)
# print(cutting.cup)