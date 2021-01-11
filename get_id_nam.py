# Sync lists of blacklisted and whitelisted URLs for CAP #
'''
This script pulls an ini list from github to use as a whitelist for CAP
'''
import configparser
import json
import requests

from epp_auth import *
from epp_ndlp_doman_whitelist_group import get_name_id_map

if __name__ == "__main__":
    epp_api_conf = configparser.ConfigParser()
    epp_api_conf.read('./epp_config.ini')

    #grab whiteist from github
    raw_wl_content = requests.get(epp_api_conf['policy']['whitelist_url'])
    new_wl_content = json.loads(raw_wl_content.text)

    #auth to epp and get token
    jwt = get_token(
        base_url=epp_api_conf['epp']['base_url'],
        username=epp_api_conf['epp']['username'],
        password=epp_api_conf['epp']['password']
        )

    test = get_name_id_map(base_url=epp_api_conf['epp']['base_url'], jwt=jwt)
    for keys, values in test.items():
        print(keys, values)