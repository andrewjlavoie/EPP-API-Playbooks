# Sync lists of blacklisted and whitelisted URLs for CAP #
'''
This script pulls an ini list from github to use as a whitelist for CAP
'''
import configparser
import json
import requests

from epp_auth import *
from epp_ndlp_doman_whitelist_group import *

if __name__ == "__main__":
    epp_api_conf = configparser.ConfigParser('./epp_config.ini')

    #grab whiteist from github
    raw_wl_content = requests.get(epp_api_conf).content
    new_wl_content = json.load(raw_wl_content.text)

    #auth to epp and get token
    jwt = get_token(
        base_url=epp_api_conf['epp']['base_url'],
        username=epp_api_conf['epp']['username'],
        password=epp_api_conf['epp']['password']
        )

    #patch new whitelist to current white list
    for whitelist in new_wl_content:
        wl_items = []
        for item in whitelist:
            wl_items.append(
                {'word': item}
            )
            
        patch_ndlp_domain_whitelist_group(
            base_url=epp_api_conf['epp']['base_url'],
            jwt=jwt,
            name=whitelist,
            desc='',
            items=new_wl_content[whitelist]
        )