import random
from app import app
from flask import json

__CONTENT_TYPE_JSON = "application/json"
__CONTENT_TYPE_IMAGE = "multipart/form-data"

def test_create_data():

    response = app.test_client().get('/data')
    data_before = json.loads(response.data.decode('utf-8'))
    
    payload = {
        "label":"Uva",
        'nitrogen' : 80,
        'phosphor' : 30,
        'potassium' : 45,
        'temperature' : 25,
        'humidity' : 10

    }


    response_post = app.test_client().post('/data', data = json.dumps(payload),content_type= __CONTENT_TYPE_JSON)
    response_post = app.test_client().post('/data', data = json.dumps(payload),content_type= __CONTENT_TYPE_JSON)
    response_post = app.test_client().post('/data', data = json.dumps(payload),content_type= __CONTENT_TYPE_JSON)
    response_post = app.test_client().post('/data', data = json.dumps(payload),content_type= __CONTENT_TYPE_JSON)
    response_post = app.test_client().post('/data', data = json.dumps(payload),content_type= __CONTENT_TYPE_JSON)
    
    response = app.test_client().get('/data')
    data_after = json.loads(response.data.decode('utf-8'))
    
    assert response_post.status_code == 200
    assert len(data_before) + 5 == len(data_after)

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


def test_update_data():

    response = app.test_client().get('/data')
    data_response = json.loads(response.data.decode('utf-8'))
    data_to_put = data_response[-1]

    payload = {
        "label": data_to_put['label'] + ' TEST',
        "nitrogen" : data_to_put['nitrogen'] + 1,
        'phosphor' : data_to_put['phosphor'] + 1,
        'potassium' : data_to_put['potassium'] + 1,
        'temperature' : data_to_put['temperature'] + 1,
        'humidity' : data_to_put['humidity'] + 1
        
    }

    response_put = app.test_client().put(f'data/{data_to_put["id"]}', content_type=__CONTENT_TYPE_JSON, data=json.dumps(data_to_put))

    response = app.test_client().get(f'/data/{data_to_put["id"]}')
    data = json.loads(response.data.decode('utf-8'))

    assert response_put.status_code == 200
    assert data['id'] == data_to_put['id']
    assert data['label'] != data_to_put['label']
    assert data['nitrogen'] != data_to_put['nitrogen']
    assert data['phosphor'] != data_to_put['phosphor']
    assert data['potassium'] != data_to_put['potassium']
    assert data['humidity'] != data_to_put['humidity']
    assert data['temperature'] != data_to_put['temperature']

def test_delete_data():

    response = app.test_client().get('/data')
    data = json.loads(response.data.decode('utf-8'))
    
    response_del = app.test_client().delete(f'data/{data[-1]["id"]}')

    response = app.test_client().get('/data')
    data_after = json.loads(response.data.decode('utf-8'))

    assert response_del.status_code == 200
    assert len(data) - 1 == len(data_after)