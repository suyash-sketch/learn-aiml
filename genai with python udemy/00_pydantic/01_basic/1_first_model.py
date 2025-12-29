from pydantic import BaseModel

class User(BaseModel):
    id : int
    name : str
    is_active : bool

input_data  = { 'id' : 101, 'name' : "ChaiCode", 'is_active' :2 }

user = User(**input_data)   # ** is spread operator to unpack the dictionary

print(user)