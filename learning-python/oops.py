class Factory:
    a = 12

    def hello(self):
        print("Hello world")

    print("hello how are you i am getting initialized")

obj = Factory()

print(obj.a)
obj.hello()

class Animal:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print(f"hello your name is {self.name}")

class Human(Animal):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age
    
    def show(self):
        print(f"hello your name is {self.name} and age is {self.age}")
    
animal1 = Animal("lion")

person1 = Human("suyash",20)

person1.show() 

animal1.show()


#Comprehesion

l = [i for i in range(1,21) if i % 2 == 0]

print(l)

d = {i : i**2 for i in range(1,10)}

print(d)