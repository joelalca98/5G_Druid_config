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
    #Parse core_info
    core_info = Druid_json['core_info']
    amf_iface = core_info['amf_iface']
except:
    logging.critical('The parameter amf is not defined in config file')
    sys.exit(-1)

try:
    amf_port = core_info['amf_port']    #Optional
except:
    amf_port = cons.amf_port

try:
    mme_iface = core_info['mme_iface']
except:
    logging.critical('The parameter mme is not defined in config file')
    sys.exit(-1)

try:
    mme_port = core_info['mme_port']    #Optional
except:
    mme_port = cons.mme_port

try:
    mgw_iface = core_info['mgw_iface']
except:
    logging.critical('The parameter mgw in not defined in config file')
    sys.exit(-1)

    #Parse plmn_info
try:
    plmn_info = Druid_json['plmn_info']
    mcc = plmn_info ['mcc']
    mnc = plmn_info ['mnc']
    network_name = plmn_info ['network_name']
except:
    logging.critical('One of the main parameters of plmn are not defined in config file')
    sys.exit(-1)
  