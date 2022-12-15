import asyncio
from pathlib import Path

from src.sense_t.daw.aa.supply_chain_api.config import config, set_config
from src.sense_t.daw.aa.supply_chain_api.db import db
from src.sense_t.daw.aa.supply_chain_api.auth import generateToken

TEST_CONFIG = {
    "db": "sqlite+aiosqlite://",
    "jwt_key": "J74YjNoG32nqYami9R0HaXsgQ3FtErsTbYQYJ8ZywE4",
    "redirects": {
        "invalid_uid": "https://daw-aa.sense-t.net/invalid_uid"
    },
    "static": str((Path(__file__).parent / '../static').resolve())
}
AUTH_HEADER = {'Authorization': None}


async def _asyncInit():
    await db.TestInit(config['db'])


def initTest():
    set_config(TEST_CONFIG)
    AUTH_HEADER['Authorization'] = f'Bearer {generateToken(1)}'
    asyncio.run(_asyncInit())