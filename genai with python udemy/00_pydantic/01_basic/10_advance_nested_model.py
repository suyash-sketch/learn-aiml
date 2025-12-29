from pydantic import BaseModel
from typing import List, Optional, Union

class Address(BaseModel):
    city : str
    street : str
    postal_code : str

class Company(BaseModel):
    name : str
    address : Optional[Address] = None

class Employee(BaseModel):
    e_name : str
    company : Optional[Company] = None   # employee can be free lancer so there might be or not might be a company


#another type to write 
class TextContent(BaseModel):
    type : str = "text"  ## text : str
    content : str

class ImageContent(BaseModel):
    type : str = "Image"  ## Image : str
    type : str = "url"

class Article(BaseModel):
    title : str
    sections : List[Union[TextContent, ImageContent]]


# Deeply Nested Structure
class Country(BaseModel):
    name : str
    code : str

class State(BaseModel):
    name : str
    country : Country

class City(BaseModel):
    name : str
    state : State

class Address(BaseModel):
    street : str
    city : City
    postal_code : str

class Organizaton(BaseModel):
    name : str
    headquarter : Address
    branches : List[Address] = []

