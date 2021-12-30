import requests
from requests.auth import HTTPBasicAuth
from utils import Core_parser
from utils import Subnet_parser
from utils import Sims_parser
from utils import Core
from utils import Users
from utils import Subnet
from utils import Request
from utils.Users import Users
from utils import Users


request = Request 
parserCore = Core
parseUser = Users
parserSubnet = Subnet

def main():
         core = Core.Core(parserCore.Core_parser)
         core.call_core(parserCore.Core_parser)
         user = Users.Users(parseUser.Sims_parser)
         user.call_user(parseUser.Sims_parser)
         subnet = Subnet.Subnet(parserSubnet.Subnet_parser)
         subnet.call_subnet(parserSubnet.Subnet_parser) 
   

# core = Core.Core(parserCore.Core_parser)
# core.call_core(parserCore.Core_parser)
# user = Users.Users(parseUser.Sims_parser)
# user.call_user(parseUser.Sims_parser)
# subnet = Subnet.Subnet(parserSubnet.Subnet_parser)
# subnet.call_subnet(parserSubnet.Subnet_parser) 

if __name__ == '__main__':
    main()
