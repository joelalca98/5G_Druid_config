import requests
import json
from requests import auth
from requests.auth import HTTPBasicAuth
from utils import Core_parser
from utils import Subnet_parser
from utils import Constant
from utils import Druid_parser
import logging


cons = Constant

http = HTTPBasicAuth(username=Druid_parser.username,password=Druid_parser.password)

class Request:
    def __init__(self, url, auth, args):
        self.url = url
        self.auth = auth
        self.args = args

    def putCall (self, url, args, type):
    
        try:
            response = requests.put(url, auth=http, verify=False, json = args)
        except Exception as e:
            logging.critical("Exception" + " " + type + " " + str(e))
            return -1
        if(response.status_code == 200):
            response_info = response.json()
            print(response_info)
            return 0
        elif(response.status_code == 401):
            logging.critical("Error in auth")
        elif(response.status_code == 404):
            logging.critical("Error in the CORE call")
        else :
            logging.critical("Error code %d", response.status_code)
        return -1

    def postCall (self, url, args):
        
        try:
            response = requests.post(url, auth=http, verify=False, json = args)
        except Exception as e:
            logging.critical("Exception" +" " + str(e))
            return -1
        if(response.status_code == 200):
            response_info = response.json()
            print(response_info)
            return 0
        elif(response.status_code == 401):
            logging.critical("Error in auth")
        elif(response.status_code == 404):
            logging.critical("Error url")
        else :
            logging.critical("Error code %d", response.status_code)
        return -1

    def delCall (self, url, args):
        try:
            response = requests.delete(url, auth=http, verify=False, json = args)
            response_info = response.json
            print(response_info)
            return response_info
        except:
            logging.critical("Error in the DELETE call")
            return -1

            