'''
This script is a framework for generating OTP for CAP
Use: > create_cap_otp.py [duration] [computer] [justification]
ie: > create_cap_otp.py '15 min' andrew-pc 'need to test'
'''
import configparser
import json
import requests
import sys

from epp_auth import get_token
from epp_computer import get_computers_id_name_map
from epp_otp import post_otp

if __name__ == "__main__":
    epp_api_conf = configparser.ConfigParser()
    epp_api_conf.read('./epp_config.ini')

    #auth to epp and get token
    print('Authenticating to EPP MC -- Get JWT')
    jwt = get_token(
        base_url=epp_api_conf['epp']['base_url'],
        username=epp_api_conf['epp']['username'],
        password=epp_api_conf['epp']['password']
        )
    print(f'Bearer JWT: {jwt}')

    #get computer to id
    computer_to_id = get_computers_id_name_map(
        base_url=epp_api_conf['epp']['base_url'],
        jwt=jwt
        )

    #create otp
    new_otp = post_otp(
        base_url=epp_api_conf['epp']['base_url'],
        jwt=jwt,
        otp_type=3,
        duration=sys.argv[1],
        machine_id=computer_to_id[sys.argv[2]],
        justification=sys.argv[3]
    )

    #return the OTP
    print('Generated OTP :' + new_otp['otp_code'])