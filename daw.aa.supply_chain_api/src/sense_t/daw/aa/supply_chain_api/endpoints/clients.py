from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_utils.cbv import cbv
from sqlalchemy import exc

from ..auth import JWTBearer
from ..dals.client import ClientDAL
from ..dals.product_type import ProductTypeDAL
from ..dtos.client import ClientCreateDTO, ClientUpdateDTO
from ..dtos.product_type import ProductTypeDTO

client_router = APIRouter()


@cbv(client_router)
class ClientCBV():
    auth: dict = Depends(JWTBearer())
    client_dal: ClientDAL = Depends(ClientDAL.GetDAL)
    product_type_dal: ProductTypeDAL = Depends(ProductTypeDAL.GetDAL)

    @client_router.get("/clients", tags=["Clients"])
    async def list_clients(self):
        """List clients"""
        return await self.client_dal.getAllClients()

    @client_router.post("/clients", tags=["Clients"])
    async def create_client(self, new_client: ClientCreateDTO):
        """Create new client"""
        try:
            return await self.client_dal.createClient(new_client.name,
                                                      new_client.product_url,
                                                      new_client.description,
                                                      new_client.icon)

        except exc.IntegrityError:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Client with that name already exists")

    @client_router.get("/client/{id}", tags=["Clients"])
    async def get_client(self, id: int):
        """Get client details"""
        client = await self.client_dal.getClient(id)
        if client is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Client not found")
        return client

    @client_router.put("/client/{id}", tags=["Clients"])
    async def update_client(self, id: int, client_update: ClientUpdateDTO):
        """Update client details"""
        try:
            return await self.client_dal.updateClient(
                id, client_update.name, client_update.product_url,
                client_update.description, client_update.icon)

        except exc.IntegrityError:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail="Client with that name already exists")

    # @client_router.delete("/client/{id}", tags=["Clients"])
    # async def delete_client(id: int):
    #     """Delete/Disable client"""
    #     return {"username": "fakecurrentuser"}

    @client_router.get("/client/{id}/validations", tags=["Clients"])
    async def get_client_validations(self, id: int):
        """List validations for this client"""
        return await self.client_dal.getClientValidations(id)

    @client_router.get("/client/{id}/product_types", tags=["Clients"])
    async def get_client_product_types(self, id: int):
        """List product types for this client"""
        return await self.client_dal.getClientProductTypes(id)

    @client_router.post("/client/{id}/product_types", tags=["Clients"])
    async def create_new_product_type(self, id: int,
                                      product_type: ProductTypeDTO):
        """Create new product type for this client"""
        return await self.product_type_dal.createProductType(
            id, product_type.name, product_type.description)
