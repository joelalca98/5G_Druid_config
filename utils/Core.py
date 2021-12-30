import requests
from requests import auth
from requests.auth import HTTPBasicAuth
from utils import Core_parser
from utils import Subnet_parser
from utils.Request import Request
from utils import Constant
from utils import Druid_parser
import logging

druid = Druid_parser
request = Request
cons = Constant
logging.basicConfig(filename='app.log', level='DEBUG')

class Core:
    def __init__(self, parser):
        self.amf_iface = parser.amf_iface
        self.amf_port = parser.amf_port
        self.mme_iface = parser.mme_iface
        self.mme_port = parser.mme_port
        self.mgw_iface = parser.mgw_iface
        self.mcc = parser.mcc
        self.mnc = parser.mnc
        self.network_name = parser.network_name
        
    def call_core (self, parser): #Aplicar try
        IP_AMF = 'https://' + druid.base_ip + ':443' '/api' '/amf?id=1'
        argsAmf = { 
        'n2_net_device' : parser.amf_iface,
        'n2_port': parser.amf_port
               }
        #Modify MME
        BASE_IP_MME = 'https://' + druid.base_ip + ':443' '/api' '/mme?id=1'
        argsMme = { 
        's1mme_net_device' : parser.mme_iface,
        's1mme_port': parser.mme_port
               }
        #Modify mgw https://192.168.40.124/api/mgw_endpoint?id=1
        BASE_IP_MGW = 'https://' + druid.base_ip + ':443' '/api' '/mgw_endpoint?id=1'
        argsMgw = { 
           'net_device': parser.mgw_iface
        }
        #Modify PLMN 'https://192.168.40.124:443/api/plmn?id=1'
        BASE_IP_PLMN = 'https://' + druid.base_ip + ':443' '/api' '/plmn?id=1'
        argsPlmn = { 
           'mcc': parser.mcc,
           'mnc': parser.mnc,
           'short_network_name': parser.network_name,
           'full_network_name': parser.network_name
        }
        counter = 1
        while(counter <= cons.number):
            if (request.putCall(request,IP_AMF,argsAmf, cons.typeAmf) == -1): #Try the first call (3)
           
                logging.critical('Failed attempt')
                counter = counter + 1
                if counter > cons.number:
                    exit()
            else: #If the first call goes right, I apply the other calls
                request.putCall(request,BASE_IP_MME,argsMme, cons.typeMme)
                request.putCall(request, BASE_IP_MGW, argsMgw, cons.typeMgw)
                request.putCall(request,BASE_IP_PLMN,argsPlmn, cons.typePlmn)
                logging.info('CORE modified correctly')
                counter = cons.number + 1
                
        
        


