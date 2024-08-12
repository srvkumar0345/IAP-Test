import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_version(client):
    rv = client.get('/version')
    assert rv.status_code == 200
    json_data = rv.get_json()
    assert json_data['version'] == '1.0.0'
    assert json_data['description'] == 'pre-interview technical test'
