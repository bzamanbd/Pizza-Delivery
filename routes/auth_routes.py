from fastapi import APIRouter,Depends 
from sqlalchemy.orm import Session 
from dependencies import SessionGenerator
from schemas import SignUpSchema
from models import User
from exceptions import UserExistException
from utility import getUserByEmail, createUser

auth_router = APIRouter( prefix="/api", tags=["Auth"]) 

@auth_router.post("/signup",status_code=201)
def create_user(user:SignUpSchema, db:Session = Depends(SessionGenerator)):
    db_user:User | None = getUserByEmail(db, email=user.email) 
    if db_user:
        raise UserExistException
    return createUser( db, user=user)



