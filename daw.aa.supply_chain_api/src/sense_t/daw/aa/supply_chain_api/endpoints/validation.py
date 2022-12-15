from datetime import datetime, timezone
from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from fastapi_utils.cbv import cbv
from starlette.datastructures import URL

from ..config import config
from ..dals.product import ProductDAL

validation_router = APIRouter()


@cbv(validation_router)
class NoAuthValidationCBV():
    product_dal: ProductDAL = Depends(ProductDAL.GetDAL)

    @validation_router.get("/v/{uid}", tags=["Validation"])
    async def validate_product_mac(self, request: Request, uid: str):
        """Validate product NFC tag, will redirect"""

        redirect_url = await self.product_dal.validateProduct(
            uid, datetime.now(timezone.utc), request.client.host,
            dict(request.headers), str(request.url), request.method)

        if redirect_url is None:
            return RedirectResponse(url=config['redirects']['invalid_uid'])

        url = URL(redirect_url).include_query_params(uid=uid, valid=True)
        return RedirectResponse(url)
