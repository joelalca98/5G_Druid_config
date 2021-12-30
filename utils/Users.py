from typing import NoReturn
import requests
from requests import NullHandler, auth
from requests.auth import HTTPBasicAuth
from utils import Core_parser
from utils import Subnet_parser
from utils.Request import Request
from utils import Sims_parser
from utils import Constant
from utils import Druid_parser
import logging

logging.basicConfig(filename='app.log', level='DEBUG')
druid = Druid_parser
request = Request
constant = Constant

class Users:
    def __init__(self, parser):
        self.ki = parser.ki
        self.opc = parser.opc
    def call_user (self, parser): 
        list = parser.ue_list
        num = len(list)
        counter = 1 
        try:
            list[num-1]
            while (counter <= num): 
                    try: 
                        for x in list:
                            IP_S1 = 'https://' + druid.base_ip + ':443' '/api' '/subscriber'
                            qos = x['qos']
                            argsU = { 
                            'imsi' : x['imsi'], #try and except and log warning
                            'name': x['friendly_name'],
                            'ki' : parser.ki,
                            'opc' : parser.opc,
                            'authorised' : "1",
                            'auth_algorithm' : "milenage",
                            'ciphering_algorithm' : "best",
                            "dl_ambr": qos['dl_ambr'],
                            "ul_ambr": qos['ul_ambr']
                                } 
                            response = request.postCall(request,IP_S1,argsU)
                            counter = counter + 1
                            if (response==-1):
                                logging.info('Error creating the user')
                            else:
                                logging.info('User created correctly')

                    except: 
                            name = constant.friendly_name
                            for x in list:
                                IP_S1 = 'https://' + druid.base_ip + ':443' '/api' '/subscriber'
                                argsU = { 
                                'imsi' : x['imsi'],

                                'name': name + str(counter),  #Convert to string
                                'ki' : parser.ki,
                                'opc' : parser.opc,
                                'authorised' : "1",
                                'auth_algorithm' : "milenage",
                                'ciphering_algorithm' : "best",
                                "dl_ambr": constant.dl_umbr,
                                "ul_ambr": constant.ul_ambr
                                    }   
                                res = request.postCall(request,IP_S1,argsU)
                                counter = counter + 1
                                logging.info(res)
                                if (res==-1):
                                    logging.info('Error creating the user')
                                else:
                                    logging.info('User created correctly')
                                    logging.warning('Constant variables are being used')

        except:
              logging.critical('The parameter IMSI is not defined ')
              exit()




    
