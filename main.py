from fastapi import FastAPI 
from database import Base, Engine
from routes import RootRouter, AuthRouter, OrderRouter 
app = FastAPI()

Base.metadata.create_all(bind=Engine)

app.include_router(RootRouter)
app.include_router(AuthRouter)
app.include_router(OrderRouter)