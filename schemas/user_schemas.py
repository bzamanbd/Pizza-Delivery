from pydantic import BaseModel 

class UserBase(BaseModel):
    username: str
    email: str
    is_active:bool | None
    is_staff: bool | None

class SignUpSchema(UserBase):
    password:str