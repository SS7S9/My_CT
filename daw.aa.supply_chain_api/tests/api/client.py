from fastapi.testclient import TestClient

from src.sense_t.daw.aa.supply_chain_api.api import app
from ..setup import initTest, AUTH_HEADER

client = TestClient(app)

initTest()


def test_newClient():
    response = client.post('/api/clients',
                           json={
                               "name": "Test Client",
                               "description": "Just a small test client",
                               "product_url": "daw_aa.sense-t.net/validator",
                           },
                           headers=AUTH_HEADER)
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Test Client",
        "description": "Just a small test client",
        "product_url": "daw_aa.sense-t.net/validator",
        "icon": None
    }


def test_ListClients():
    response = client.get('/api/clients', headers=AUTH_HEADER)
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "name": "Test Client",
        "description": "Just a small test client",
        "product_url": "daw_aa.sense-t.net/validator",
        "icon": None,
        "deleted": None
    }]


def test_updateClient():
    response = client.put('/api/client/1',
                          json={
                              "name": "Test Client",
                              "description":
                              "Just a small test client - updated",
                              "product_url": "daw_aa.sense-t.net/validator",
                          },
                          headers=AUTH_HEADER)
    assert response.status_code == 200


def test_getClient():
    response = client.get('/api/client/1', headers=AUTH_HEADER)
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "name": "Test Client",
        "description": "Just a small test client - updated",
        "product_url": "daw_aa.sense-t.net/validator",
        "icon": None,
        "deleted": None,
    }


def test_getValidations():
    response = client.get('/api/client/1/validations', headers=AUTH_HEADER)
    assert response.status_code == 200
    assert response.json() == []


def test_newProductType():
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


def test_getProductTypes():
    response = client.get('/api/client/1/product_types', headers=AUTH_HEADER)
    assert response.status_code == 200
    assert response.json() == [{
        "id": 1,
        "client_id": 1,
        "name": "Test Product Type",
        "description": "Some product type",
        "active": None,
        "inactive": None
    }]