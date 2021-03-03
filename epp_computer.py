import requests

# api calls

def get_computers(base_url, jwt):
    '''Gets a list of all computers'''
    response = requests.get(
        base_url+'/api/computer',
        headers={'Authorization': jwt}
    )
    return response.json()


# tools

def get_computers_id_name_map(base_url, jwt):
    #get all
    all_computers = get_computers(base_url, jwt)
    name_to_id = {}

    for group in all_computers['items']:
        print(group['id'], group['name'])
        name_to_id[group['name']] = group['id']

    return name_to_id