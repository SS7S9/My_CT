from .clients import client_router
from .product_type import product_type_router
from .products import product_router
from .validation import validation_router
from .details import details_router

from fastapi import APIRouter

apiRouter = APIRouter(prefix='/api')
apiRouters = [
    client_router, product_type_router, product_router, details_router
]
for router in apiRouters:
    apiRouter.include_router(router)

routers = [apiRouter, validation_router]