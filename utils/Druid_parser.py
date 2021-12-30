import argparse
import requests
from requests import auth
from requests.auth import HTTPBasicAuth
import json
import sys
import logging
from utils import Constant
import data

logging.basicConfig(filename='app.log', level='DEBUG')
cons = Constant
Druid_json = data.Druid_json

try:
    #Parse druid_info
    druid_info = Druid_json['druid_info']
    username = druid_info['username']
    password = druid_info['password']
    base_ip = druid_info['base_ip']
except:
    logging.critical('One of the main parameters of druid_info are not defined in config file')
    sys.exit(-1)