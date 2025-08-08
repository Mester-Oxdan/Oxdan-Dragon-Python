from msvcrt import getch
import subprocess
import imports.own.will_go_to_start
from colorama import Fore
import colorama
import ctypes
from imports.own.my_wifi_pas_start import my_wifi_pas_start
from imports.own.inject_prog_start import inject_prog_start
from imports.own.inject_prog_2_start import inject_prog_2_start
from imports.own.cor_desk_start import cor_desk_start
from imports.own.ascii_code_start import ascii_code_start
from imports.own.pas_gen_n_start import pas_gen_n_start
from imports.own.pas_gen_u_start import pas_gen_u_start
from imports.own.pas_gen_w_start import pas_gen_w_start
from imports.own.pas_gen_nw_start import pas_gen_nw_start
from imports.own.ip_search import ip_search
from imports.own.phone_search import phone_search
from imports.own.auto_clicker_start import auto_clicker_start
from imports.own.wifi_hack_start import wifi_hack_start
from imports.own.get_ip_site_start67 import get_ip_site_start
from imports.own.morse_code_start import morse_code_start
from imports.own.cuaser_cipher_start import cuaser_cipher_start
from imports.own.con_wifi_start import con_wifi_start
from msvcrt import getche
from time import sleep
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
from phonenumbers.util import u
import pycountry , phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from geopy.geocoders import Nominatim
import os

STD_OUTPUT_HANDLE = -11
hStdOut = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

def ConsoleCursorVisible(show, size):
    class CursorInfo(ctypes.Structure):
        _fields_ = [("size", ctypes.c_int),
                    ("visible", ctypes.c_byte)]

    cursor_info = CursorInfo()
    ctypes.windll.kernel32.GetConsoleCursorInfo(hStdOut, ctypes.byref(cursor_info))
    cursor_info.visible = show
    cursor_info.size = size
    ctypes.windll.kernel32.SetConsoleCursorInfo(hStdOut, ctypes.byref(cursor_info))

def Hacker_Stuffs():

    if imports.own.will_go_to_start.x.lower() == "my_wifi_pas": # my_wifi_pas (+)

        try:

            my_wifi_pas_start()

        except:

            imports.own.will_go_to_start.main()
            
    if imports.own.will_go_to_start.x.lower() == "mimikatz": # mimikatz (+)

        try:

            os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\mimikatz-master\\mimikatz-master\\x64\\mimikatz.exe")
            #print(os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\mimikatz-master\\mimikatz-master\\x64\\mimikatz.exe")
            #os.system(str(result))
            imports.own.will_go_to_start.main()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "metasploit": # metasploit (+)

        try:

            os.system('"' + '"' + "C:\metasploit\console.bat" + '"' + '"')
            imports.own.will_go_to_start.main()

        except:
            print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install metasploit!)" + colorama.Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "aircrack-ng": # aircrack-ng (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command = imports.own.will_go_to_start.writex.lower().split()
                command.remove("aircrack-ng")
                # Execute the pip command
                #result = subprocess.run(command, capture_output=True, text=True)
                os.system('"' + '"' + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\aircrack-ng\\aircrack-ng_1\\bin\\aircrack-ng.exe" + '"' + '"' + ' ' + ''.join(command))
                # Print the output of the command
                #print(result.stdout)
                #print(result)
                #os.system(result)
                imports.own.will_go_to_start.main()

        except:
            #print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install metasploit!)" + colorama.Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "sqlmap": # sqlmap (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command = imports.own.will_go_to_start.writex.lower().split()
                command.remove("sqlmap")
                # Execute the pip command
                #result = subprocess.run(command, capture_output=True, text=True)
                #print('"' + '"' + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\sqlmap\\sqlmap.py" + '"' + '"' + ' ' + ''.join(command))
                os.system("python " + '"' + '"' + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\sqlmap\\sqlmap.py" + '"' + '"' + ' ' + ''.join(command))
                # Print the output of the command
                #print(result.stdout)
                #print(result)
                #os.system(result)
                imports.own.will_go_to_start.main()

        except:
            #print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install metasploit!)" + colorama.Fore.WHITE)
            imports.own.will_go_to_start.main()
            
    if imports.own.will_go_to_start.writex.lower().startswith("john"): # john (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command = imports.own.will_go_to_start.writex.lower().split()
                command.remove("john")
                # Execute the pip command
                #result = subprocess.run(command, capture_output=True, text=True)
                result = os.system('"' + '"' + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\john_the_ripper\\run\\john.exe" + '"' + '"' + ' ' + ''.join(command))
                # Print the output of the command
                #print(result.stdout)
                #print(result)
                os.system(result)
                imports.own.will_go_to_start.main()

        except:

           #print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install python-3.10.6!)" + colorama.Fore.WHITE)
           imports.own.will_go_to_start.main()
           
    if imports.own.will_go_to_start.writex.lower().startswith("nmap"): # nmap (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command = imports.own.will_go_to_start.writex.lower().split()
                #command.remove("nmap")
                # Execute the pip command
                os.system(' '.join(command))
                #result = subprocess.run(command, capture_output=True, text=True)
                #result = os.system(os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\john_the_ripper\\run\\john.exe " + ''.join(command))
                # Print the output of the command
                #print(result.stdout)
                #print(result)
                imports.own.will_go_to_start.main()

        except:

           print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install nmap!)" + colorama.Fore.WHITE)
           imports.own.will_go_to_start.main()
           
    if imports.own.will_go_to_start.writex.lower().startswith("hydra"): # hydra (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command = imports.own.will_go_to_start.writex.lower().split()
                command.remove("hydra")
                # Execute the pip command
                #result = subprocess.run(command, capture_output=True, text=True)
                result =  os.system('"' + '"' + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\hydra_windows\\hydra.exe" + '"' + '"' + ' ' + ''.join(command))
                # Print the output of the command
                #print(result.stdout)
                #print(result)
                os.system(result)

                """# Remove "hydra" from the command list
                command = [cmd for cmd in command if cmd != "hydra"]

                # Get environment variable
                oxdan_dragon_w = os.environ["OXDAN-DRAGON-PYTHON"]

                # Construct the command
                separator = " "
                right_command = f"\"{oxdan_dragon_w}\\imports\\own\\imports\\john_the_ripper\\run\\john.exe\""
                right_command = f"\"{right_command}\""

                # Add remaining commands
                right_command += separator + separator.join(command)

                # Execute the command
                subprocess.run(right_command, shell=True)"""

                imports.own.will_go_to_start.main()

        except:

           #print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install python-3.10.6!)" + colorama.Fore.WHITE)
           imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "xsstrike": # xsstrike (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command = imports.own.will_go_to_start.writex.lower().split()
                command.remove("xsstrike")
                # Execute the pip command
                #result = subprocess.run(command, capture_output=True, text=True)
                os.system("python " + '"' + '"' + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\XSStrike\\xsstrike.py" + '"' + '"' + ' ' + ''.join(command))
                # Print the output of the command
                #print(result.stdout)
                #print(result)
                #os.system(result)
                imports.own.will_go_to_start.main()

        except:
            #print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install metasploit!)" + colorama.Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "slowloris": # slowloris (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command = imports.own.will_go_to_start.writex.lower().split()
                command.remove("slowloris")
                # Execute the pip command
                #result = subprocess.run(command, capture_output=True, text=True)
                os.system("python " + '"' + '"' + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\slowloris\\slowloris.py" + '"' + '"' + ' ' + ''.join(command))
                # Print the output of the command
                #print(result.stdout)
                #print(result)
                #os.system(result)
                imports.own.will_go_to_start.main()

        except:
            #print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install metasploit!)" + colorama.Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "tbomb": # tbomb (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command = imports.own.will_go_to_start.writex.lower().split()
                command.remove("tbomb")
                # Execute the pip command
                #result = subprocess.run(command, capture_output=True, text=True)
                os.system("python " + '"' + '"' + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\TBomb\\bomber.py" + '"' + '"' + ' ' + ''.join(command))
                # Print the output of the command
                #print(result.stdout)
                #print(result)
                #os.system(result)
                imports.own.will_go_to_start.main()

        except:
            #print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install metasploit!)" + colorama.Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "ihulk": # ihulk (+)

        try:

                print(" ")
                # Split the input into a list of command-line arguments
                command = imports.own.will_go_to_start.writex.lower().split()
                command.remove("ihulk")
                # Execute the pip command
                #result = subprocess.run(command, capture_output=True, text=True)
                os.system("python " + '"' + '"' + os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\ihulk.py\\src\\ihulk.py" + '"' + '"' + ' ' + ''.join(command))
                # Print the output of the command
                #print(result.stdout)
                #print(result)
                #os.system(result)
                imports.own.will_go_to_start.main()

        except:
            #print(colorama.Fore.RED + "(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Install metasploit!)" + colorama.Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "morse_code_cipher": # morse_code_cipher (+)

        try:

            morse_code_start()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "caesar_cipher": # caesar_cipher (+)

        try:

            cuaser_cipher_start()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "con_wifi": # con_wifi (+)

        try:

            con_wifi_start()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "get_ip_website": # get_ip_website (+)

        try:

                #defret = input(Fore.YELLOW + "\nEnter website name with (.com): " + Fore.WHITE)
                tokens = imports.own.will_go_to_start.writex.split(" ")
                name = tokens[1]
                get_ip_site_start(name)

        except:

            print(colorama.Fore.RED + "\n(!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Site did not found!)" + colorama.Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "auto_clicker": # auto_clicker (+)

        try:

            auto_clicker_start()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "ip_search": # ip_search (+)

        try:

            ip_search()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter network ip address!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "phone_search": # phone_search (+)

        try:

            phone_search()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter Phone Number With Country Code!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "wifi_hack": # wifi_hack (+)

        try:

            wifi_hack_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "dll_injector": # dll_injector (+)

        try:

            inject_prog_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "cor_desk": # cor_desk (+)

        ConsoleCursorVisible(False, 100);

        try:

                cor_desk_start()

        except KeyboardInterrupt:

                imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "ascii_code": # ascii_code (+)
            
        try:

            ascii_code_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "pas_gen": # pas_gen (+)

        try:

                    tokens = imports.own.will_go_to_start.writex.split(" ")
                    name = tokens[1]

                    if name == "w": # pas gen w (+)
            
                        try:

                            pas_gen_w_start()

                        except:

                            imports.own.will_go_to_start.main()

                    if name == "u": # pas gen u (+) 
            
                        try:

                            pas_gen_u_start()

                        except:

                            imports.own.will_go_to_start.main()

                    if name == "n": # pas gen n (+) 
            
                        try:

                            pas_gen_n_start()

                        except:

                            imports.own.will_go_to_start.main()

                    if name.lower() == "nw": # pas gen nw (+) 
            
                        try:

                            pas_gen_nw_start()

                        except:

                            imports.own.will_go_to_start.main()
                    else:
                        print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter pas gen option!)\n" + Fore.WHITE)
                        imports.own.will_go_to_start.main()
        except:
                    
                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter pas gen option!)\n" + Fore.WHITE)
                    imports.own.will_go_to_start.main()