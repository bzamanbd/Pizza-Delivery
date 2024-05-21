from fastapi import APIRouter

root_router =APIRouter(tags=["Root"]) 

@root_router.get('/',status_code= 200) 
def root()->str:
    return 'Welcome, this is root router'

