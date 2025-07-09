import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_create_and_get_dataset(client):
    res = client.post('/datasets', json={
        'name': 'Test',
        'owner': 'bob',
        'description': 'desc',
        'tags': ['test']
    })
    assert res.status_code == 201
    dataset_id = res.get_json()['id']
    res = client.get(f'/datasets/{dataset_id}')
    assert res.status_code == 200
    data = res.get_json()
    assert data['name'] == 'Test'
