import whois
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#pip3 install python-whois

def is_registered(domain_name):
    """
    A function that returns a boolean indicating 
    whether a `domain_name` is registered
    """
    try:
        w = whois.whois(domain_name)
    except Exception:
        return False
    else:
        return bool(w.domain_name)

domain = sys.argv[1]
print (bcolors.OKCYAN + " \n Checking Domain \n" + bcolors.ENDC)

if is_registered(domain):
	print (bcolors.BOLD + bcolors.OKGREEN + domain +' is registered\n'+ bcolors.ENDC)
	whois_info = whois.whois(domain)
	print (bcolors.BOLD + "\nDomain registrar:" , whois_info.registrar + bcolors.ENDC)
	print (bcolors.BOLD + "\nWHOIS server:" , whois_info.whois_server + bcolors.ENDC)
	#print (bcolors.BOLD + "\nDomain creation date:", whois_info.creation_date,'' + bcolors.ENDC)
	#print (bcolors.BOLD + "\nExpiration date:" + whois_info.expiration_date,'' + bcolors.ENDC)
	print (bcolors.BOLD + "\n", whois_info,'' + bcolors.ENDC)
else: 
	print  (bcolors.WARNING + domain + ' is not registered\n' + bcolors.ENDC)






