from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_utils.cbv import cbv
from sqlalchemy import exc

from ..auth import JWTBearer
from ..dals.product_type import ProductTypeDAL
from ..dals.product import ProductDAL
from ..dtos.product_type import ProductTypeDTO

product_type_router = APIRouter()


@cbv(product_type_router)
class ProductTypeCBV():
    auth: dict = Depends(JWTBearer())
    product_type_dal: ProductTypeDAL = Depends(ProductTypeDAL.GetDAL)
    product_dal: ProductDAL = Depends(ProductDAL.GetDAL)

    @product_type_router.get("/product_types", tags=["Product Type"])
    async def list_product_types(self):
        """List product types"""
        return await self.product_type_dal.getAllProductTypes()

    @product_type_router.get("/product_type/{id}", tags=["Product Type"])
    async def get_product_type(self, id: int):
        """Get product type details"""
        client = await self.product_type_dal.getProductType(id)
        if client is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Product type not found")
        return client

    @product_type_router.put("/product_type/{id}", tags=["Product Type"])
    async def update_product_type(self, id: int, product_type: ProductTypeDTO):
        """Update product type details"""
        try:
            return await self.product_type_dal.updateProductType(
                id, product_type.name, product_type.description,
                product_type.active, product_type.inactive)

        except exc.IntegrityError:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Unable to create product type")

    # @product_type_router.delete("/product_type/{id}", tags=["Product Type"])
    # async def delete_product_type(self, id: int):
    #     """Delete/Disable product type"""
    #     return {"username": "fakecurrentuser"}

    @product_type_router.get("/product_type/{id}/validations",
                             tags=["Product Type"])
    async def get_product_type_validations(self, id: int):
        """List validations for this product type"""
        return await self.product_type_dal.getProductTypeValidations(id)

    @product_type_router.post("/product_type/{id}/register/{uid}",
                              tags=["Product Type"])
    async def create_product(self, id: int, uid: str):
        """Register a new product"""
        try:
            return await self.product_dal.createProduct(id, uid)

        except exc.IntegrityError:
            raise HTTPException(
                status_code=409,
                detail="Unable to create product - UID already exists")
