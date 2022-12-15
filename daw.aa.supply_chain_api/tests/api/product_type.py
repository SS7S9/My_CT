from fastapi.testclient import TestClient

from src.sense_t.daw.aa.supply_chain_api.api import app
from ..setup import initTest, AUTH_HEADER

client = TestClient(app)

initTest()


def test_newProductType():
    response = client.post('/api/clients',
                           json={
                               "name": "Test Client",
                               "description": "Just a small test client",
                               "product_url": "daw_aa.sense-t.net/validator",
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
    assert response.json() == {
        "id": 1,
        "client_id": 1,
        "name": "Test Product Type",
        "description": "Some product type",
    }


def test_ListProductTypes():
    response = client.get('/api/product_types', headers=AUTH_HEADER)
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "client_id": 1,
        "name": "Test Product Type",
        "description": "Some product type",
        "active": None,
        "inactive": None
    }]


def test_updateProductType():
    response = client.put('/api/product_type/1',
                          json={
                              "name": "Test Product Type",
                              "description": "Some product type - updated",
                          },
                          headers=AUTH_HEADER)
    assert response.status_code == 200


def test_getProductType():
    response = client.get('/api/product_type/1', headers=AUTH_HEADER)
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "client_id": 1,
        "name": "Test Product Type",
        "description": "Some product type - updated",
        "active": None,
        "inactive": None
    }


def test_createProduct():
    response = client.post('/api/product_type/1/register/SOME_MAC',
                           headers=AUTH_HEADER)
    assert response.status_code == 200
    assert response.json() == {"product_type_id": 1, "uid": "SOME_MAC"}


def test_getValidations():
    response = client.get('/api/product_type/1/validations',
                          headers=AUTH_HEADER)
    assert response.status_code == 200
    assert response.json() == []
