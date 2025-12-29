from typing import Optional
from pydantic import BaseModel, Field

class Employee(BaseModel):
    id : int
    name : str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples="Suyash Khandagale",
    )
    department : Optional[str] = 'General'
    salary : float = Field(
        ge=10000             # ge = greater than equal to
    )