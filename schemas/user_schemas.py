from pydantic import BaseModel 


class UserBase(BaseModel):
    id: int | None
    username: str
    email: str
    is_active:bool | None
    is_staff: bool | None

class SignUpSchema(UserBase):
    password:str

    class Config():
        orm_mode= True
        schema_extra = { 
            'example':{ 
                'username':'Ripon',
                'email':'ripon@gmail.com',
                'password':'password',
                'is_active':'True',
                'is_staff':'False'
            }
        }