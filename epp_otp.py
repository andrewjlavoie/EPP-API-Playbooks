import requests

def get_otp(base_url, otp_id, jwt):
    '''Gets a single Offline Temporary Password'''
    response = requests.get(
        base_url+'/api/otp/'+otp_id,
        headers={'Authorization': jwt}
    )
    return response.json()

def get_otp_list(base_url, jwt):
    '''Gets a list of Offline Temporary Passwords'''
    response = requests.get(
        base_url+'/api/otp',
        headers={'Authorization': jwt}
    )
    return response.json()

def get_transfer_limit(base_url, jwt):
    '''Gets a single Offline Temporary Password'''
    response = requests.get(
        base_url+'/api/otp/transferLimit',
        headers={'Authorization': jwt}
    )
    return response.json()

def post_otp(base_url, jwt, otp_type, duration, machine_id, justification):
    '''Creates a new Offline Temporary Password'''
    otp_ids = {
        '15 min':  '0',
        '30 min':  '1',
        '1 hour':  '2',
        '2 hours': '3',
        '4 hours': '4',
        '8 hours': '5',
        '1 day':   '6',
        '2 days':  '7',
        '5 days':  '8',
        '14 days': '9',
        '30 days': '10'
    }

    response = requests.post(
        base_url+'/api/otp',
        headers={'Authorization': jwt},
        json={
            'otp_type': otp_type,
            'otp_id': 'null',
            'duration': otp_ids[duration],
            'machine_id': machine_id,
            'justification' : justification,
            'status': 'null'
        }
    )
    return response.json()

def del_single_otp(otp_id, base_url, jwt):
    '''Delete an existing Offline Temporary Password'''
    response = requests.delete(
        base_url+'/api/otp/'+otp_id,
        headers={'Authorization': jwt}
    )
    return response.json()

def del_multi_otp(base_url, jwt):
    '''Delete existing Offline Temporary Passwords'''
    response = requests.delete(
        base_url+'/api/otp',
        headers={'Authorization': jwt}
    )
    return response.json()