from typing import Optional
from datetime import datetime
from sqlalchemy import select, update

from ..models.product_type import ProductType
from ..models.validation import Validation
from .dal import DAL


class ProductTypeDAL(DAL):

    @DAL.withCTX
    async def createProductType(self,
                                client_id: int,
                                name: str,
                                description: Optional[str] = None,
                                session=None):

        new_product_type = ProductType(client_id=client_id,
                                       name=name,
                                       description=description)
        session.add(new_product_type)
        await session.flush()
        return new_product_type

    @DAL.withCTX
    async def getAllProductTypes(self, session=None):
        q = await session.execute(select(ProductType))
        return q.scalars().all()

    @DAL.withCTX
    async def getProductType(self, product_type_id: int, session=None):
        q = await session.execute(
            select(ProductType).where(ProductType.id == product_type_id))
        product_type = q.scalar()
        return product_type

    @DAL.withCTX
    async def updateProductType(self,
                                product_type_id: int,
                                name: Optional[str],
                                description: Optional[str],
                                active: Optional[datetime],
                                inactive: Optional[datetime],
                                session=None):
        q = update(ProductType).where(ProductType.id == product_type_id)

        if name is not None:
            q = q.values(name=name)

        if description is not None:
            q = q.values(description=description)

        if active is not None:
            q = q.values(active=active)

        if inactive is not None:
            q = q.values(inactive=inactive)

        q.execution_options(synchronize_session="fetch")
        await session.execute(q)

    @DAL.withCTX
    async def getProductTypeValidations(self,
                                        product_type_id: int,
                                        session=None):
        q = await session.execute(
            select(Validation).where(
                (Validation.product_type_id == product_type_id)).order_by(
                    Validation.request_time))
        return q.scalars().all()