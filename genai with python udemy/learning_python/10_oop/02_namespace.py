class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = True

print(Chai.is_hot)

#creating objects from chai

masala = Chai()

print(masala.origin)
print(masala.is_hot)

masala.is_hot = False

print("Class value: ", Chai.is_hot)

print("Object value: ", masala.is_hot )