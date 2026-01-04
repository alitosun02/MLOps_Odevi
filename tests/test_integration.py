import pytest
import json
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_predict_endpoint(client):
    response = client.post('/predict', 
                           data=json.dumps({'text': 'TestMloPs'}),
                           content_type='application/json')
    
    assert response.status_code == 200
    data = response.get_json()
    assert 'bucket' in data
    assert isinstance(data['bucket'], int)

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.get_json() == {'status': 'ok'}