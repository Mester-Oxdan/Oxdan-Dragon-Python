import socket
import imports.own.will_go_to_start
from colorama import Fore

def get_ip_site_start(defret):

    fre = socket.gethostbyname(str(defret))
    print(" ")
    print(Fore.YELLOW + "Ip address of " + Fore.WHITE + defret + Fore.YELLOW + " is: " + Fore.WHITE + str(fre))
    imports.own.will_go_to_start.main()
