from .root_route import root_router as RootRouter
from .auth_routes import auth_router as AuthRouter
from .order_routes import order_router as OrderRouter
__all__:list[str] = ["RootRouter","AuthRouter","OrderRouter"]