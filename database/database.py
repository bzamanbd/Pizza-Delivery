from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql://postgres:1234@localhost/pizza_delivery"

Engine = create_engine(DB_URL, echo=True) 

Base = declarative_base()
SessionLocal = sessionmaker(bind=Engine)