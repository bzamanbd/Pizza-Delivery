from models import User
from sqlalchemy.orm import Session 
from schemas import SignUpSchema 
from werkzeug.security import generate_password_hash

def get_user(db: Session, user_id: int)->User | None:
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str)->User | None:
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100)->list[User]:
    return db.query(User).offset(skip).limit(limit).all() 

def create_user(db: Session, user: SignUpSchema)->User:
    # fake_hashed_password = user.password + "notreallyhashed"
    new_user = User( 
    id = user.id,
    username = user.username,
    email = user.email,
    password = generate_password_hash(user.password),
    is_active = user.is_active,
    is_staff = user.is_staff
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
