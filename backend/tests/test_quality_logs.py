def test_add_and_list_quality_log(client):
    res = client.post('/datasets', json={
        'name': 'QTest',
        'owner': 'alice',
        'description': 'desc',
        'tags': []
    })
    dataset_id = res.get_json()['id']
    res = client.post(f'/datasets/{dataset_id}/quality-1', json={
        'status': 'PASS',
        'details': 'All good',
        'dataset_id': dataset_id
    })
    assert res.status_code == 201
    res = client.get(f'/datasets/{dataset_id}/quality-1')
    assert res.status_code == 200
    logs = res.get_json()
    assert len(logs) > 0
    assert logs[0]['status'] == 'PASS'
