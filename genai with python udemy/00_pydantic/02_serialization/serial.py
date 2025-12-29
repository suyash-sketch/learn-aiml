from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street : str
    city : str
    postal_code : str 


class User(BaseModel):
    id : int
    name : str
    email : str
    is_active : bool = True
    createdAt : datetime
    address : Address
    tags : List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime : lambda v : v.strftime('%d-%m-%Y %H:%M:%S')}
    )

user = User(
    id= 1,
    name="Suyash",
    email="suyash@gmail.com",
    is_active=False,
    createdAt=datetime(2024, 3, 15, 14, 30, 20),
    address=Address(
        street="Nothing",
        city="Panvel",
        postal_code="400101",
    ),
    tags=['premium', 'subscriber']
)

python_dict = user.model_dump()
print(user)
print("="*100)
print(python_dict)
print("="*100)


json_str = user.model_dump_json()
print(json_str)