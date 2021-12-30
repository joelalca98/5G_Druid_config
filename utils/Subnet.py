import requests
from requests import auth
from requests.auth import HTTPBasicAuth
from utils import Core_parser
from utils import Subnet_parser
from utils import Request
import requests
from requests import auth
from requests.auth import HTTPBasicAuth
from utils import Core_parser
from utils import Subnet_parser
from utils import Sims_parser
from utils.Request import Request
from utils import Druid_parser
import logging

druid = Druid_parser
request = Request
logging.basicConfig(filename='app.log', level='DEBUG')

class Subnet:
    def __init__(self, parser):
        self.apn = parser.apn
        self.tun_addr_ip = parser.tun_addr_ip
        self.tun_netmask = parser.tun_netmask
        self.ipv4_pool_first_ip = parser.ipv4_pool_first_ip
        self.ipv4_pool_last_ip = parser.ipv4_pool_last_ip
        #QoS
        self.qci = parser.qci
        self.dl_apn_ambr = parser.dl_apn_ambr
        self.ul_apn_ambr = parser.ul_apn_ambr
        self.priority = parser.priority
        self.may_trigger_preemption = parser.may_trigger_preemption
        self.preemptable = parser.preemptable
        
    def call_subnet (self, parser):
       
       #Create ipv4_pool  OK
        IP_SPP = 'https://' + druid.base_ip + ':443' '/api' '/ipv4_pool'
        args = { 
                   "id": 3,
                   "name": parser.apn,
                   "first_ip" : parser.ipv4_pool_first_ip,
                   "last_ip" : parser.ipv4_pool_last_ip
               }
        resIpv4 = request.postCall(request, IP_SPP, args)
        if (resIpv4 == -1):
               logging.warning('Error creating ipv4 pool')
        else:
            logging.info('ipv4 created')
       
        #Create subnet    OK
        IP_CreateSubnet = 'https://' + druid.base_ip + ':443' '/api' '/pdn'
        args = { 
                   "id": 6,
                   "apn": parser.apn,
                   "primary_dns": "8.8.8.8",
                   "secondary_dns": "8.8.4.4",
                   "ipv4_pool_id": 3,
                   "ep_group_id": 2,
                   "allow_multiple_connections": 0
               }

        resCreate = request.postCall(request, IP_CreateSubnet, args)
        if ( resCreate == -1):
               logging.warning('Error in creating the subnet')
        else:
            logging.info('The subnet was created correctly')

        #Activate subnet create previously   OK
        IP_ActivateSubnet = 'https://' + druid.base_ip + ':443' '/api' '/subscription_profile'
        args = { 
                   "id": 6,
                   "apn": parser.apn,
                   "qci": parser.qci,
                   "priority": parser.priority,
                   "may_trigger_preemption": parser.may_trigger_preemption,
                   "preemptable": parser.preemptable,
                   "network_slice_id": 1,
                   "dl_apn_ambr": parser.dl_apn_ambr,
                   "ul_apn_ambr": parser.ul_apn_ambr,
                   "apply_to_all_subs": 0
               }
        resActivate = request.postCall(request, IP_ActivateSubnet, args)
        if ( resActivate == -1):
               logging.warning('Error in activate the subnet')
        else:
            logging.info('Subnet activated correctly') #Hasta aqui

        #Delete other networks
        #Delete Network 1     OK
        IP_DeleteSubnets1 = 'https://' + druid.base_ip + ':443' '/api' '/pdn?id=1'  
        args = { 
               }
        resDel1 = request.delCall(request, IP_DeleteSubnets1, args)
        logging.info('Delete subnet 1 status:')
        logging.info(resDel1)
        #Delete Network 2  
        IP_DeleteSubnets2 = 'https://' + druid.base_ip + ':443' '/api' '/pdn?id=2'
        args = { 
               }
        resDel2 = request.delCall(request, IP_DeleteSubnets2, args)
        logging.info('Delete subnet 2 status:')
        logging.info(resDel2)
       
        #Delete Network 3   
        IP_DeleteSubnets3 = 'https://' + druid.base_ip + ':443' '/api' '/pdn?id=3'
        args = { 
               }
        resDel3 = request.delCall(request, IP_DeleteSubnets3, args)
        logging.info('Delete subnet 3 status:')
        logging.info(resDel3)
        #Delete Network 4  
        IP_DeleteSubnets4 = 'https://' + druid.base_ip + ':443' '/api' '/pdn?id=4'
        args = { 
               }
        resDel4 = request.delCall(request, IP_DeleteSubnets4, args)
        logging.info('Delete subnet 4 status:')
        logging.info(resDel4)
        #Create Subscription_Profile_Preference   OK
        IP_SPP = 'https://' + druid.base_ip + ':443' '/api' '/subscription_profile_preference'
        args = { 
                   "id": 1,
                   "name": parser.apn,
                   "subscription_profile_1_id": 6,
                   "subscription_profile_2_id": 0,
                   "subscription_profile_3_id": 0,
                   "subscription_profile_4_id": 0,
                   "subscription_profile_5_id": 0
               }
        resSubs= request.postCall(request,IP_SPP, args)
        if ( resSubs == -1):
               logging.warning('Error in the subsctiption profile preference')
        else:
            logging.info('Subscription profile preference added correctly')
        #Create Group   OK
        IP_Group = 'https://' + druid.base_ip + ':443' '/api' '/group'
        args = { 
                   "id": 1,
                   "num": "1",
                   "name": parser.apn,
                   "imsi_prefix": "",
                   "description": parser.apn,
                   "subscription_profile_preference_id":1
               }

        resCreateGroup = requests.post(IP_Group, auth=HTTPBasicAuth(username=druid.username,password=druid.password),verify=False, json=args)
        logging.info('Group status:')
        logging.info(resCreateGroup)

        #Add ip and netmask
        IP_NET = 'https://' + druid.base_ip + ':443' '/api' '/net_device?id=1'
        args = {
                   "ip": parser.tun_addr_ip,
                   "netmask": parser.tun_netmask
               }
        resAdd =requests.put(IP_NET, auth=HTTPBasicAuth(username=druid.username,password=druid.password),verify=False, json=args)
        if (resAdd == -1):
               logging.warning('Can not modify the net device')
        else:
            logging.info('ip and netmask modified correctly')
        #Add the group
        counter = 1
        listUser = []
        listUser = parser.ue_list
        num = len(listUser)
        while (counter <= num):
              IP_Sup = 'https://' + druid.base_ip + ':443' '/api' '/group' '/subscribers'
              args = { 
                     "id": counter,
                     "group_id": "1",
                     "subscriber_id": counter,
                     }
              resAd = requests.post(IP_Sup, auth=HTTPBasicAuth(username=druid.username,password=druid.password),verify=False, json=args)
              counter = counter + 1
        logging.info('Add the group status:')
        logging.info(resAd)
        

        
        