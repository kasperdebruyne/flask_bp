def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b'Hello from flask!' in res.data