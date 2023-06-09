import random
from app import app
from flask import json

__CONTENT_TYPE_JSON = "application/json"
__CONTENT_TYPE_IMAGE = "multipart/form-data"

def test_create_data():

    response = app.test_client().get('/data')
    data_before = json.loads(response.data.decode('utf-8'))
    
    payload = {
        "label":"Top demais",
        'nitrogen' : 1,
        'phosphor' : 1,
        'potassium' : 1,
        'temperature' : 1,
        'humidity' : 1

    }

    response_post = app.test_client().post('/data', data = json.dumps(payload),content_type= __CONTENT_TYPE_JSON)
    
    response = app.test_client().get('/data')
    data_after = json.loads(response.data.decode('utf-8'))
    
    assert response_post.status_code == 200
    assert len(data_before) + 1 == len(data_after)

def test_get_all_data():
    response = app.test_client().get('/data')
    data = json.loads(response.data.decode('utf-8'))
    
    assert response.status_code == 200
    assert len(data) > 0

def test_get_data_by_id():

    response = app.test_client().get('/data')
    data = json.loads(response.data.decode('utf-8'))

    data_id = data[-1]['id']
    response = app.test_client().get(f'/data/{data_id}')
    data = json.loads(response.data.decode('utf-8'))
    
    assert response.status_code == 200
    assert data['id'] == data_id

def test_delete_data():

    response = app.test_client().get('/data')
    data = json.loads(response.data.decode('utf-8'))
    
    response_del = app.test_client().delete(f'data/{data[-1]["id"]}')

    response = app.test_client().get('/data')
    data_after = json.loads(response.data.decode('utf-8'))

    assert response_del.status_code == 200
    assert len(data) - 1 == len(data_after)