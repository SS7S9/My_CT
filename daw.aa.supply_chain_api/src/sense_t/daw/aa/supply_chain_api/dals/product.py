from datetime import datetime, timezone
from sqlalchemy import select, update

from ..models.clients import Client
from ..models.product_type import ProductType
from ..models.product import Product
from ..models.validation import Validation

from .dal import DAL


class ProductDAL(DAL):
    """Data Access Layer to provide access to product management"""

    @DAL.withCTX
    async def createProduct(self,
                            product_type_id: int,
                            uid: str,
                            session=None):

        new_product = Product(product_type_id=product_type_id, uid=uid)
        session.add(new_product)
        await session.flush()
        return new_product

    @DAL.withCTX
    async def getProductValidations(self, uid: str, session=None):
        q = await session.execute(
            select(Validation).where(Validation.product_uid == uid).order_by(
                Validation.request_time))
        return q.scalars().all()

    @DAL.withCTX
    async def getProduct(self, uid: str, session=None):
        q = await session.execute(select(Product).where(Product.uid == uid))
        product = q.scalar()
        return product

    @DAL.withCTX
    async def validateProduct(self,
                              uid: str,
                              request_time: datetime,
                              request_source: str,
                              request_headers: dict,
                              request_url: str,
                              request_method: str,
                              session=None):
        """Validate request
        """
        validation_details = {
            'request_time': request_time,
            'request_product_uid': uid,
            'request_source': request_source,
            'request_headers': request_headers,
            'request_url': request_url,
            'request_method': request_method
        }
        product = await self.getProduct(uid)

        if product is None:
            validation = Validation(**validation_details)

        else:
            validation = Validation(product_uid=product.uid,
                                    product_type_id=product.product_type_id,
                                    **validation_details)

        session.add(validation)
        await session.flush()

        if product is None:
            return None

        q = await session.execute(
            select(Client).where((ProductType.id == validation.product_type_id)
                                 & (ProductType.client_id == Client.id)
                                 & (ProductType.inactive.is_(None)
                                    | (ProductType.inactive >= request_time))
                                 & (ProductType.active.is_(None)
                                    | (ProductType.active <= request_time))))
        client = q.scalar()

        if client is None:
            return None

        return client.product_url

    @DAL.withCTX
    async def getProductDetails(self, uid: str, session=None):
        product_details = await session.execute(
            select(
                Product.uid,
                Product.registered_at,
                ProductType.name.label('product_name'),
                ProductType.description.label('product_description'),
                Client.name.label('client_name'),
                Client.description.label('client_description'),
            ).where((Product.uid == uid)
                    & (Product.product_type_id == ProductType.id)
                    & (ProductType.client_id == Client.id)))
        try:
            return dict(product_details.__next__())

        except StopIteration:
            return None