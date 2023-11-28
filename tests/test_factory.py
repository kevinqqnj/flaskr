from flaskr import create_app

def test_config():
    # 默认不是Testing模式
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing

def test_hello(client):
    rsp = client.get('/hello')
    assert rsp.data == b'Hello, World!'