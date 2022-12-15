from urllib.parse import parse_qsl
from fastapi.testclient import TestClient
from starlette.datastructures import URL

from src.sense_t.daw.aa.supply_chain_api.api import app
from ..setup import initTest, AUTH_HEADER

client = TestClient(app)

initTest()


def test_invalidUID():
    response = client.get('/v/SOME_INVALID_MAC', allow_redirects=False)
    assert response.status_code == 307
    assert response.headers[
        'Location'] == 'https://daw-aa.sense-t.net/invalid_uid'


def test_newProduct():
    response = client.post('/api/clients',
                           json={
                               "name":
                               "Test Client",
                               "description":
                               "Just a small test client",
                               "product_url":
                               "https://daw_aa.sense-t.net/validator",
                           },
                           headers=AUTH_HEADER)
    assert response.status_code == 200
    response = client.post('/api/client/1/product_types',
                           json={
                               "name": "Test Product Type",
                               "description": "Some product type",
                           },
                           headers=AUTH_HEADER)
    assert response.status_code == 200

    response = client.post('/api/product_type/1/register/SOME_MAC',
                           headers=AUTH_HEADER)
    assert response.status_code == 200
    assert response.json() == {"product_type_id": 1, "uid": "SOME_MAC"}


def test_getValidations():
    response = client.get('/api/product/SOME_MAC/validations',
                          headers=AUTH_HEADER)
    assert response.status_code == 200
    assert response.json() == []
