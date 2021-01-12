import requests

def get_token(base_url, username, password):
    ''' returns value from k,v {'token': 'xxx'} '''
    if base_url[-1] == '/':
        base_url = base_url[:-1]
    response = requests.post(
        base_url+'/api/login',
        json={'username': username, 'password': password}
        )
    return 'Bearer '+response.json()['token']