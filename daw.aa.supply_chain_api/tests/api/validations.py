from datetime import datetime, timezone, timedelta
from urllib.parse import parse_qsl
from fastapi.testclient import TestClient
from starlette.datastructures import URL

from src.sense_t.daw.aa.supply_chain_api.api import app
from ..setup import initTest, AUTH_HEADER

client = TestClient(app)

initTest()


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


def test_invalidUID():
    response = client.get('/v/SOME_INVALID_MAC', allow_redirects=False)
    assert response.status_code == 307
    assert response.headers[
        'Location'] == 'https://daw-aa.sense-t.net/invalid_uid'


def test_validUID():
    response = client.get('/v/SOME_MAC', allow_redirects=False)
    assert response.status_code == 307

    redirect_url = URL(response.headers['Location'])
    assert redirect_url.scheme == 'https'
    assert redirect_url.netloc == 'daw_aa.sense-t.net'
    assert redirect_url.path == '/validator'
    assert set(parse_qsl(redirect_url.query)) == {('uid', 'SOME_MAC'),
                                                  ('valid', 'True')}


def test_getClientValidations():
    response = client.get('/api/client/1/validations', headers=AUTH_HEADER)
    assert response.status_code == 200

    validations = response.json()
    assert len(validations) == 1
    validation = validations[0]

    assert validation['product_uid'] == 'SOME_MAC'
    assert validation['product_type_id'] == 1
    assert validation['request_url'] == 'http://testserver/v/SOME_MAC'
    assert validation['request_product_uid'] == validation['product_uid']


def test_getProductTypeValidations():
    response = client.get('/api/product_type/1/validations',
                          headers=AUTH_HEADER)
    assert response.status_code == 200

    validations = response.json()
    assert len(validations) == 1
    validation = validations[0]

    assert validation['product_uid'] == 'SOME_MAC'
    assert validation['product_type_id'] == 1
    assert validation['request_url'] == 'http://testserver/v/SOME_MAC'
    assert validation['request_product_uid'] == validation['product_uid']


def test_getProductValidations():
    response = client.get('/api/product/SOME_MAC/validations',
                          headers=AUTH_HEADER)
    assert response.status_code == 200

    validations = response.json()
    assert len(validations) == 1
    validation = validations[0]

    assert validation['product_uid'] == 'SOME_MAC'
    assert validation['product_type_id'] == 1
    assert validation['request_url'] == 'http://testserver/v/SOME_MAC'
    assert validation['request_product_uid'] == validation['product_uid']


def test_checkAllValidations():
    response = client.get('/api/validations', headers=AUTH_HEADER)
    assert response.status_code == 200

    validations = response.json()
    assert len(validations) == 2

    assert validations[0]['product_uid'] is None
    assert validations[0]['product_type_id'] is None
    assert validations[0][
        'request_url'] == 'http://testserver/v/SOME_INVALID_MAC'
    assert validations[0]['request_product_uid'] == 'SOME_INVALID_MAC'

    assert validations[1]['product_uid'] == 'SOME_MAC'
    assert validations[1]['product_type_id'] == 1
    assert validations[1]['request_url'] == 'http://testserver/v/SOME_MAC'
    assert validations[1]['request_product_uid'] == validations[1][
        'product_uid']


def test_productDetails():
    response = client.get('/api/details/SOME_MAC', headers=AUTH_HEADER)
    assert response.status_code == 200

    data = response.json()
    assert data == {
        'uid': 'SOME_MAC',
        'registered_at': data['registered_at'],
        'product_name': 'Test Product Type',
        'product_description': 'Some product type',
        'client_name': 'Test Client',
        'client_description': 'Just a small test client'
    }


def test_expiredProduct():
    response = client.get('/v/SOME_MAC', allow_redirects=False)
    assert response.status_code == 307

    redirect_url = URL(response.headers['Location'])
    assert redirect_url.scheme == 'https'
    assert redirect_url.netloc == 'daw_aa.sense-t.net'
    assert redirect_url.path == '/validator'
    assert set(parse_qsl(redirect_url.query)) == {('uid', 'SOME_MAC'),
                                                  ('valid', 'True')}

    response = client.put('/api/product_type/1',
                          json={
                              "inactive": (datetime.now(timezone.utc) -
                                           timedelta(seconds=1)).isoformat(),
                          },
                          headers=AUTH_HEADER)
    assert response.status_code == 200

    response = client.get('/v/SOME_MAC', allow_redirects=False)
    assert response.status_code == 307
    assert response.headers[
        'Location'] == 'https://daw-aa.sense-t.net/invalid_uid'