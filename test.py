import requests
from requests import auth
from requests.auth import HTTPBasicAuth
import argparse
import requests
from requests import auth
from requests.auth import HTTPBasicAuth
import json
import sys
import logging

from requests.sessions import Request

request = Request

inputfile = 'C:/Users/Alcalde/Desktop/Demo/Druid.json'

with open (inputfile) as f:
    Druid_json = json.load(f)
    #Parse druid_info
druid_info = Druid_json['druid_info']
username = druid_info['username']
password = druid_info['password']
base_ip = druid_info['base_ip']
core_info = Druid_json['core_info']
amf_iface = core_info['amf_iface']
amf_port = core_info['amf_port']
sims_info = Druid_json['sims_info']
ki = sims_info['ki']
opc = sims_info['opc']
ue_list = []
ue_list = sims_info['ue_list']
subnet_info = Druid_json['subnet_info']
apn = subnet_info['apn']
tun_addr_ip = subnet_info['tun_addr_ip']
tun_netmask = subnet_info['tun_netmask']
ipv4_pool_first_ip = subnet_info['ipv4_pool_first_ip']
ipv4_pool_last_ip = subnet_info['ipv4_pool_last_ip']
sims_info = Druid_json['sims_info']
qos = subnet_info['qos']
qci = qos['qci']

num = len(ue_list)
print(num)
for x in ue_list:
    imsi = x['imsi']
    print (len(imsi))
    print (imsi)

http = HTTPBasicAuth(username=username,password=password)
url = 'https://' + base_ip + ':443' '/api' '/amf?id=1'
USERNAME = username
PASSWORD = password
argsAmf = { 
    'n2_net_device' : amf_iface
               }

def test_core():
    response = requests.put(url, auth=http, verify=False, json=argsAmf)
    print(response.json())
    assert response.status_code == 200

def test_users():
    assert len(imsi)>0
    
IP_CreateSubnet = 'https://' + base_ip + ':443' '/api' '/pdn'
args = { 
            "id": 6,
            "apn": apn,
            "primary_dns": "8.8.8.8",
            "secondary_dns": "8.8.4.4",
        }
def test_subnet():
    response = requests.post(IP_CreateSubnet, auth=http, verify=False, json=args)
    assert response.status_code != 200