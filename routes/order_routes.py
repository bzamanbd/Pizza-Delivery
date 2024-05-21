from fastapi import APIRouter
order_router = APIRouter(prefix="/api",tags=["Order"])

@order_router.post("/order", status_code=201)
async def make_order()->str: 
    return 'Order placed'