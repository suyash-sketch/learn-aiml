from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street : str
    city : str
    postal_code : str 

class User(BaseModel):
    id : int
    name : str
    address : Address      # model inside a model (nested class)

address = Address(
    street='backstreet 21b',
    city='panvel',
    postal_code='410218'
)

user = User(
    id=12,
    name='Suyash',
    address=address
)


# Another way
user_data = {
    'id' : 123,
    'name' : 'Suyash',
    'address' : {
        'street' : 'kings circle',
        'city' : 'mumbai',
        'postal_code' : '400001'
    }
}

user2 = User(**user_data)
print(user2)
print(user)