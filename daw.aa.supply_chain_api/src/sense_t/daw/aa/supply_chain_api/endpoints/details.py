from fastapi import APIRouter, Depends
from fastapi_utils.cbv import cbv

from ..auth import JWTBearer
from ..dals.validation import ValidationDAL
from ..dals.product import ProductDAL

details_router = APIRouter()


@cbv(details_router)
class NoAuthDetailsCBV():
    product_dal: ProductDAL = Depends(ProductDAL.GetDAL)

    @details_router.get("/details/{uid}", tags=["Validation"])
    async def product_details(self, uid: str):
        """Get product details (No auth)"""
        product = await self.product_dal.getProductDetails(uid)
        return product


@cbv(details_router)
class AuthValidationCBV():
    auth: dict = Depends(JWTBearer())
    validation_dal: ValidationDAL = Depends(ValidationDAL.GetDAL)

    @details_router.get("/validations", tags=["Validation"])
    async def list_product_validations(self):
        """List product validations"""
        return await self.validation_dal.getValidations()