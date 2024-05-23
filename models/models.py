from database import Base 
from sqlalchemy import Column,Integer, String,Boolean,ForeignKey
from sqlalchemy.orm import relationship 
from sqlalchemy_utils.types import ChoiceType

class User(Base): 
    __tablename__:str = "users"
    id = Column(Integer, autoincrement=True,primary_key=True)
    username = Column(String(50),index=True) 
    email = Column(String(50), unique=True ) 
    password = Column(String, nullable=True) 
    is_active = Column(Boolean, default=True)
    is_staff = Column(Boolean, default=False)
    orders = relationship("Order", back_populates="owner")
    
    def __repr__(self):
        return "User {self.username}"


class Order(Base): 
    ORDER_STATUS=( 
        ('PENDING','pending'), 
        ('PROCESSING','processing'), 
        ('DELIVERED','delivered')
    )

    PIZZA_SIZES=( 
        ('SMALL','small'), 
        ('MEDIUM','medium'), 
        ('LARGE','large'),
        ('EXTRA-LARGE','extra-large')
    )

    __tablename__:str = "orders"
    id = Column(Integer, autoincrement=True, primary_key=True) 
    quantity = Column(Integer) 
    order_status = Column(ChoiceType(choices = ORDER_STATUS),default="PENDING")
    pizza_size = Column(ChoiceType(choices = PIZZA_SIZES), default="SMALL")
    flavour = Column(String(25)) 
    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("User", back_populates="orders")

    def __repr__(self):
        return "Order {self.id}"



