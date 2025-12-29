from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price : float
    in_stock : bool = True

product1 = Product(id=1, name="Laptop", price=999.99, in_stock=True)
product2 = Product(id=2, name="Mouse", price=23.33)

product3 = Product(name="Mouse")
