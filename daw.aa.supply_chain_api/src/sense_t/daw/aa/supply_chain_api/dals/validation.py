from sqlalchemy import select, update

from ..models.validation import Validation

from .dal import DAL


class ValidationDAL(DAL):
    @DAL.withCTX
    async def getValidations(self, session=None):
        q = await session.execute(
            select(Validation).order_by(Validation.request_time))
        return q.scalars().all()
