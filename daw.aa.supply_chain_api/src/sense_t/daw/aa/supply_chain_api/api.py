from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .endpoints import routers
from .config import config
from .db import db

app = FastAPI()

if 'cors' in config:
    app.add_middleware(CORSMiddleware, **config.get('cors', {}))

for router in routers:
    app.include_router(router)

# I've removed static files from the API, they should be hosted by the proxy
# static_files = Path(__file__).parent / 'static'
# if static_files.is_dir():
#     print(f'Static files mounted: {static_files}')
#     app.mount('/', SPAStaticFiles(directory=static_files, html=True))

# else:
#     print('Static files not mounted: Static dir does not exist')


@app.on_event("startup")
async def startup():
    await db.InitDB(config['db'])