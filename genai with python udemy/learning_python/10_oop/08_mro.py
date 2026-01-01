class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala Blend"

class C(A):
    label = "C: Herbal Blend"

class D(C, B):
    pass

cup = D()
print(cup.label)
print(D.__mro__)