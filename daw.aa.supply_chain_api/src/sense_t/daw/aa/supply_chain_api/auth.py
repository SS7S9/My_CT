from datetime import datetime, timezone, timedelta
import jwt

from fastapi import Request, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from .config import config

class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")

            try:
                return jwt.decode(credentials.credentials, config['jwt_key'], algorithms=["HS512"])

            except jwt.PyJWTError:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Could not validate credentials",
                    headers={"WWW-Authenticate": "Bearer"},
                )
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

def generateToken(expiry_days):
    iat = datetime.now(timezone.utc)
    exp = iat + timedelta(days=expiry_days)

    return jwt.encode(
        {
            'iat': int(iat.timestamp()),
            'exp': int(exp.timestamp())
        },
        config['jwt_key'],
        algorithm="HS512")
