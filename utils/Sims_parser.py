import logging
import requests
from requests import auth
from requests.auth import HTTPBasicAuth
import json
import sys
import data

logging.basicConfig(filename='app.log', level='DEBUG')
Druid_json = data.Druid_json

try:
    #Parse SIM
    sims_info = Druid_json['sims_info']
    ki = sims_info['ki']
    opc = sims_info['opc']
    ue_list = []
    ue_list = sims_info['ue_list']
    len = len(ue_list)
except Exception as e:
        logging.critical("One of the main parameters in not defined in config file: " + str(e))
        sys.exit(-1)
