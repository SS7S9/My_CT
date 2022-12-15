from ..db import db

class DAL():
    def __init__(self, shared_session=None) -> None:
        self._shared_session = shared_session
        self._ctx = None

    @staticmethod
    def withCTX(func):
        async def wrapped(self, *a, **kw):
            if self._shared_session is None:
                async with db.session() as session:
                    async with session.begin():
                        return await func(self, *a, **kw, session=session)

            else:
                return await func(self, *a, **kw, session=self._shared_session)

        return wrapped

    @classmethod
    async def GetDAL(cls):
        async with db.session() as session:
            async with session.begin():
                yield cls(session)
