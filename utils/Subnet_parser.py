import logging
import requests
from requests import auth
from requests.auth import HTTPBasicAuth
import json
import sys
from utils import Constant
import data
import logging


cons = Constant
Druid_json = data.Druid_json

#Parse Subnet
try:
        subnet_info = Druid_json['subnet_info']
        apn = subnet_info['apn']
except:
    logging.critical('The parameter apn is not defined in config file')
    sys.exit(-1)

try:
        tun_addr_ip = subnet_info['tun_addr_ip']
except:
    logging.critical('The parameter apn is not defined in config file')
    sys.exit(-1)

try:
        tun_netmask = subnet_info['tun_netmask']
except:
    logging.critical('The parameter tun_netmask is not defined in config file')
    sys.exit(-1)

try:
        ipv4_pool_first_ip = subnet_info['ipv4_pool_first_ip']
except:
    logging.critical('The parameter ipv4_pool_first_ip is not defined in config file')
    sys.exit(-1)

try:
        ipv4_pool_last_ip = subnet_info['ipv4_pool_last_ip']
except:
    logging.critical('The parameter ipv4_pool_last_ip is not defined in config file')
    sys.exit(-1)

try:
        sims_info = Druid_json['sims_info']
        ue_list = []
        ue_list = sims_info['ue_list']
except:
        logging.critical('The parameter ue_list is not defined in config file')
        sys.exit(-1)
try:
        #Parse QoS
        qos = subnet_info['qos']
        try: 
                qci = qos['qci']
        except:
                qci = cons.qci
                logging.info('Constat qci is applied')
        try:
                dl_apn_ambr = qos['dl_apn_ambr']
        except:
                dl_apn_ambr = cons.ul_apn_ambr
                logging.info('Constat dl_apn_ambr is applied')
        try:
                ul_apn_ambr = qos['ul_apn_ambr']
        except:
                ul_apn_ambr = cons.dl_apn_ambr
                logging.info('Constat ul_apn_ambr is applied')
        try:
                priority = qos['priority']
        except:
                priority = cons.priority
                logging.info('Constat priority is applied')
        try:
                may_trigger_preemption = qos['may_trigger_preemption']
        except:
                may_trigger_preemption = cons.may_trigger_preemption
                logging.info('Constat may_trigger_preemption is applied')
        try:
                preemptable = qos['preemptable']   
        except:
                preemptable = cons.preemptable
                logging.info('Constat preemptable is applied')
except:
        qci = cons.qci
        dl_apn_ambr = cons.dl_apn_ambr
        ul_apn_ambr = cons.ul_apn_ambr
        priority = cons.priority
        may_trigger_preemption = cons.may_trigger_preemption
        preemptable = cons.preemptable
        logging.warning('All QoS variables are constant')