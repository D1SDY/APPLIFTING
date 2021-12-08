def test_registration_and_login(app, client):
    """
     GIVEN a Flask application configured for testing
     WHEN the '/user/login' page is requested (GET)
     THEN check the response is valid
     """
    user = {'username': "user", "password": "123"}
    response = client.post('/user/create', json=user, follow_redirects=True)
    assert response.status_code == 200
    assert b'x-access-token' in response.data

    user = {'username': "user", "password": "123"}
    response = client.post('/user/login', json=user, follow_redirects=True)
    assert response.status_code == 200
    assert b'x-access-token' in response.data

