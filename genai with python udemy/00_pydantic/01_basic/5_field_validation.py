from pydantic import BaseModel, field_validator, model_validator


class User(BaseModel):
    username : str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError('Username must e atleast 4 characters')
        return v 

class SignUpData(BaseModel):
    password : str
    confirm_password :  str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Password do not match")
        return values