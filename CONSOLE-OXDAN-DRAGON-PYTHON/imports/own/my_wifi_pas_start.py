import imports.own.will_go_to_start
import subprocess
from colorama import Fore

def my_wifi_pas_start():

            data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
            profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

            print(" ")
            print(Fore.RED + "WIFI_PASSWORDS: " + Fore.WHITE)
            print(" ")
            print(Fore.YELLOW + "Wifi:                         " + "Passwords: " + Fore.WHITE)
            print(" ")

            for i in profiles:

                results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
                results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

                try:

                    print ("{:<30}|  {:<}".format(i, results[0]))
                    print(" ")

                except IndexError:

                    print ("{:<30}|  {:<}".format(i, ""))
                    print(" ")

            imports.own.will_go_to_start.main()