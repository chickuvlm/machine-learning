'''

This file will test the necessary interfaces during a login session.

Note: the 'pytest' instances can further be reviewed:

    - https://pytest-flask.readthedocs.io/en/latest
    - http://docs.pytest.org/en/latest/usage.html

'''

import json


def test_session(client, live_server):
    '''

    This method tests whether a redis entry is created, to represent a user
    session, for the duration of a user login.

    '''

    live_server.start()

    # local variables
    username = 'jeff1evesque'
    password = 'password123'
    payload = {'user[login]': username, 'user[password]': password}

    # login and get flask-jwt token
    login = client.post(
        '/login',
        headers={'Content-Type': 'application/json'},
        data=json.dumps(payload)
    )
    token = login.json['access_token']

    # logout
    if token:
        logout = client.post('/logout')
    else:
        assert False

    # assertion checks
    assert login.status_code == 200
    assert login.json['status'] == 0
    assert token
    assert logout.status_code == 200
    assert logout.json['status'] == 0
