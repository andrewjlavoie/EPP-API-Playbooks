import requests

# api calls

def get_ndlp_domain_whitelist_groups(base_url, jwt):
    '''Gets a list of Ndlp Domain Whitelist Groups'''
    response = requests.get(
        base_url+'/api/ndlpdomainwhitelistgroup',
        headers={'Authorization': jwt}
    )
    return response.json()

def post_ndlp_domain_whitelist_group(base_url, jwt, name, desc, items):
    '''Creates a new Ndlp Domain Whitelist Group'''
    response = requests.post(
        base_url+'/api/ndlpdomainwhitelistgroup',
        headers={'Authorization': jwt},
        json={
            'name': name,
            'description': desc,
            'cf_ndlp_domain_whitelists': items,
        }
    )
    return response.json()

def patch_ndlp_domain_whitelist_group(base_url, jwt, wl_id, name, desc, items):
    '''Updates an existing Ndlp Domain Whitelist Group'''
    '''items expects a list of dicts {'word':'site'}'''
    requests.patch(
        base_url+'/api/ndlpdomainwhitelistgroup/'+wl_id,
        headers={'Authorization': jwt},
        json={
            'name': name,
            'description': desc,
            'cf_ndlp_domain_whitelists': items,
        }
    )

def del_ndlp_domain_whitelist_group(base_url, jwt, ndlp_id):
    '''Deletes an existing Ndlp Domain Whitelist Group'''
    response = requests.delete(
        base_url+'/api/ndlpdomainwhitelistgroup/'+ndlp_id,
        headers={'Authorization': jwt},
    )
    return response.json()

# tools

def get_whitelistgroups_id_name_map(base_url, jwt):
    #get all
    all_wl = get_ndlp_domain_whitelist_groups(base_url, jwt)
    name_to_id = {}

    for group in all_wl['items']:
        print(group['id'], group['name'])
        name_to_id[group['name']] = group['id']

    return name_to_id