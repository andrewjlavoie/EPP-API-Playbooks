# Sync lists of blacklisted and whitelisted URLs for CAP #
'''
This script pulls an ini list from github to use as a whitelist for CAP
'''
import configparser
import json
import requests

from epp_auth import *
from epp_ndlp_doman_whitelist_group import get_whitelistgroups_id_name_map, patch_ndlp_domain_whitelist_group

if __name__ == "__main__":
    epp_api_conf = configparser.ConfigParser()
    epp_api_conf.read('./epp-api/epp_config.ini')

    #grab whitelist from github
    print(f'Pulling whitelist content JSON in Github')
    raw_wl_content = requests.get(epp_api_conf['policy']['whitelist_url'])
    print(f"Whitelist Location: {epp_api_conf['policy']['whitelist_url']}")
    new_wl_content = json.loads(raw_wl_content.text)

    #auth to epp and get token
    print('Authenticating to EPP MC -- Get JWT')
    jwt = get_token(
        base_url=epp_api_conf['epp']['base_url'],
        username=epp_api_conf['epp']['username'],
        password=epp_api_conf['epp']['password']
        )
    print(f'Bearer JWT: {jwt}')

    #get wl id to name map
    name_to_id = get_whitelistgroups_id_name_map(
        base_url=epp_api_conf['epp']['base_url'],
        jwt=jwt
        )
    print('Mapping Whitelistgroups ID to name in dictionary -- ID is Primary Key')

    #patch new whitelist to current white list
    print('PATCH -- Whitelists to MC')
    for whitelist in new_wl_content:
        print(f'Whitelist: {whitelist}')
        wl_items = []
        for site in new_wl_content[whitelist]:
            print(f'Whitelist item content: {site}')
            wl_items.append(
                {'word': site}
            )

        patch_ndlp_domain_whitelist_group(
            base_url=epp_api_conf['epp']['base_url'],
            jwt=jwt,
            wl_id=str(name_to_id[whitelist]),
            name=whitelist,
            desc='testtest',
            items=wl_items
        )