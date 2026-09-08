from pydantic import BaseModel


class UserSchema(BaseModel):
    name:str
    username:str
    password:str
    email:str

