import traceback
from fastapi import Response
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException


# Based on https://github.com/encode/starlette/issues/437#issuecomment-567671832
class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope) -> Response:
        response = None
        try:
            response = await super().get_response(path, scope)

        except HTTPException as e:
            if e.status_code != 404:
                raise

        if not response or response.status_code == 404:
            response = await super().get_response('.', scope)
        return response
