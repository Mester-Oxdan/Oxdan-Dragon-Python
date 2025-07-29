import requests
from colorama import Fore
from time import sleep
import imports.own.will_go_to_start

def ip_search():

            def search_net(ip='127.0.0.1'):

                    response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
                    print(Fore.RED + "\nEnter 'esc' (for exit)" + Fore.WHITE)
                    netw_ip = input(Fore.YELLOW + "Enter Network Ip Address like (" + Fore.WHITE + response.get('query') + Fore.YELLOW + "): " + Fore.WHITE)
                    
                    if imports.own.will_go_to_start.remove_098(netw_ip.lower()) == "esc":

                        imports.own.will_go_to_start.main()

                    def get_ip():
                        response65 = requests.get('https://api64.ipify.org?format=json').json()
                        return netw_ip

                    def get_location():
                        ip_address = get_ip()
                        response65 = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
                        print(" ")
                        print("COUNTRY: " + response65.get("country_name") + Fore.YELLOW + " (100% right)" + Fore.WHITE)
                        sleep(0.01)
                        print("REGION: " + response65.get("region") + Fore.YELLOW + " (100% right)" + Fore.WHITE)
                        sleep(0.01)
                        print("CITY: " + response65.get("city") + Fore.YELLOW + " (80% right)" + Fore.WHITE)
                        sleep(0.01)
                        print("ZIP: " + response65.get("postal") + Fore.YELLOW + " (80% right)" + Fore.WHITE)
                        sleep(0.01)
                        print("Y: " + str(response65.get("latitude") + 0.2522987) + Fore.YELLOW + " (100% right)" + Fore.WHITE)
                        sleep(0.01)
                        print("X: " + str(response65.get("longitude") + 0.32427346) + Fore.YELLOW + " (100% right)" + Fore.WHITE)
                        sleep(0.01)

                    get_location()
                    imports.own.will_go_to_start.main()

            response = requests.get('https://api64.ipify.org?format=json').json()
            ip = response["ip"]
                
            search_net(ip = ip)