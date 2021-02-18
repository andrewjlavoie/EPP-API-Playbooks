 Sync lists of blacklisted and whitelisted URLs for CAP #
'''
This script pulls an ini list from github to use as a whitelist for CAP
'''
import configparser
import json
import requests

from epp_auth import *
from epp_otp import *

if __name__ == "__main__":
    epp_api_conf = configparser.ConfigParser()
    epp_api_conf.read('./epp-api/epp_config.ini')

    #