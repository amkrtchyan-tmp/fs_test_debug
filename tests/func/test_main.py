def test_index(fapp):
    client = fapp.test_client()
    rv = client.get('/')
    assert 'Index view' == rv.text


def test_login(fapp):
    client = fapp.test_client()
    rv = client.post('/login', data={'email': 'admin@domain.com', "password": '123'}, follow_redirects=True)
    assert 'Secured page' == rv.text
