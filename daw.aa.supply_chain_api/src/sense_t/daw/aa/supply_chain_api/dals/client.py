from typing import Optional
from sqlalchemy import select, update

from ..models.clients import Client
from ..models.product_type import ProductType
from ..models.validation import Validation
from .dal import DAL


class ClientDAL(DAL):
    @DAL.withCTX
    async def createClient(self,
                           name: str,
                           product_url: str,
                           description: Optional[str] = None,
                           icon: Optional[str] = None,
                           session=None):
        new_client = Client(name=name,
                            product_url=product_url,
                            description=description,
                            icon=icon)
        session.add(new_client)
        await session.flush()
        return new_client

    @DAL.withCTX
    async def getAllClients(self, session=None):
        q = await session.execute(
            select(Client).where(Client.deleted == None).order_by(Client.id))
        return q.scalars().all()

    @DAL.withCTX
    async def getClient(self, client_id: int, session=None):
        q = await session.execute(
            select(Client).where((Client.deleted == None)
                                 & (Client.id == client_id)))
        client = q.scalar()
        return client

    @DAL.withCTX
    async def updateClient(self,
                           client_id: int,
                           name: Optional[str],
                           product_url: Optional[str],
                           description: Optional[str],
                           icon: Optional[str],
                           session=None):
        q = update(Client).where(Client.id == client_id)

        if name is not None:
            q = q.values(name=name)

        if product_url is not None:
            q = q.values(product_url=product_url)

        if description is not None:
            q = q.values(description=description)

        if icon is not None:
            q = q.values(icon=icon)

        q.execution_options(synchronize_session="fetch")
        await session.execute(q)

    @DAL.withCTX
    async def getClientValidations(self, client_id: int, session=None):
        q = await session.execute(
            select(Validation).where(
                (Validation.product_type_id == ProductType.id)
                & (ProductType.client_id == client_id)
                & (ProductType.client_id == client_id)).order_by(
                    Validation.request_time))
        return q.scalars().all()

    @DAL.withCTX
    async def getClientProductTypes(self, client_id: int, session=None):
        q = await session.execute(
            select(ProductType).where(ProductType.client_id == client_id))
        return q.scalars().all()
