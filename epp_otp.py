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

def post_otp(otp_type, duration, start_date, end_date, justification, base_url, jwt):
    '''Creates a new Offline Temporary Password'''
    response = requests.post(
        base_url+'/api/otp',
        headers={'Authorization': jwt},
        json={
            'otp_type': otp_type,
            'duration': duration,
            'start_date': start_date,
            'end_date': end_date,
            'justification' : justification
        }
    )
    return response

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