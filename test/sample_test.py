import random
from app import app
from flask import json

__CONTENT_TYPE_JSON = "application/json"
__CONTENT_TYPE_IMAGE = "multipart/form-data"

def test_create_data():

    response = app.test_client().get('/sample')
    data_before = json.loads(response.data.decode('utf-8'))
    
    payload = {
        "code": 1,
        "reading_Date": "2023-06-21",
        "label": 1
    }

    response_post = app.test_client().post('/sample', data = json.dumps(payload),content_type= __CONTENT_TYPE_JSON)
    
    response = app.test_client().get('/sample')
    data_after = json.loads(response.data.decode('utf-8'))
    
    assert response_post.status_code == 200
    assert len(data_before) + 1 == len(data_after)

def test_get_all_data():
    response = app.test_client().get('/sample')
    data = json.loads(response.data.decode('utf-8'))
    
    assert response.status_code == 200
    assert len(data) > 0

def test_get_data_by_id():

    response = app.test_client().get('/sample')
    data = json.loads(response.data.decode('utf-8'))

    data_id = data[-1]['id']
    response = app.test_client().get(f'/sample/{data_id}')
    data = json.loads(response.data.decode('utf-8'))
    
    assert response.status_code == 200
    assert data['id'] == data_id

def test_pacth():

    response = app.test_client().get('/sample')
    data = json.loads(response.data.decode('utf-8'))

    data_id = data[-1]['id']
    response = app.test_client().patch(f'/sample/{data_id}')

    response = app.test_client().get('/sample')
    data_aftter = json.loads(response.data.decode('utf-8'))
    
    
    assert response.status_code == 200
    assert data_aftter['label']['sample_id'] == data_id



def test_delete_data():

    response = app.test_client().get('/sample')
    data = json.loads(response.data.decode('utf-8'))
    
    response_del = app.test_client().delete(f'sample/{data[-1]["id"]}')

    response = app.test_client().get('/sample')
    data_after = json.loads(response.data.decode('utf-8'))

    assert response_del.status_code == 200
    assert len(data) - 1 == len(data_after)