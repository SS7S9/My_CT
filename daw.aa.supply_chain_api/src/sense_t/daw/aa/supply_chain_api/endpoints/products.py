from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from ..auth import JWTBearer
from ..dals.product import ProductDAL

product_router = APIRouter()


@cbv(product_router)
class ProductCBV():
    auth: dict = Depends(JWTBearer())
    product_dal: ProductDAL = Depends(ProductDAL.GetDAL)

    @product_router.get("/product/{uid}/validations", tags=["Product"])
    async def list_product_validations(self, uid: str):
        return await self.product_dal.getProductValidations(uid)
