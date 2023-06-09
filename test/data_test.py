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
        'nitrogen' : 0,
        'phosphor' : 0,
        'potassium' : 0,
        'temperature' : 0,
        'humidity' : 0

    }

    response_post = app.test_client().post('/data', data = json.dumps(payload),content_type= __CONTENT_TYPE_JSON)
    
    response = app.test_client().get('/data')
    data_after = json.loads(response.data.decode('utf-8'))
    
    assert response_post.status_code == 200
    assert len(data_before) + 1 == len(data_after)