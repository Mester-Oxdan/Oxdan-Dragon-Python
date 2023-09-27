from msvcrt import getch
import imports.own.will_go_to_start
from colorama import Fore
import colorama
import ctypes
import os
from imports.own.my_wifi_pas_start import my_wifi_pas_start
from imports.own.inject_prog_start import inject_prog_start
from imports.own.cor_desk_start import cor_desk_start
from imports.own.ascii_code_start import ascii_code_start
from imports.own.pas_gen_n_start import pas_gen_n_start
from imports.own.pas_gen_u_start import pas_gen_u_start
from imports.own.pas_gen_w_start import pas_gen_w_start
from imports.own.pas_gen_nw_start import pas_gen_nw_start
from imports.own.ip_search import ip_search
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
 
import folium
 
from opencage.geocoder import OpenCageGeocode
from phonenumbers.util import u
import pycountry , phonenumbers
from phonenumbers.phonenumberutil import region_code_for_number
from geopy.geocoders import Nominatim
from uszipcode import SearchEngine
from colorama import Fore

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
            
    if imports.own.will_go_to_start.x.lower() == "mimikatz": # my_wifi_pas (+)

        try:

            print("\n")
            os.system(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\mimikatz-master\\mimikatz-master\\x64\\mimikatz.exe"))
            #print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\mimikatz-master\\mimikatz-master\\x64\\mimikatz.exe"))
            imports.own.will_go_to_start.main()

        except:

            imports.own.will_go_to_start.main()
            
    if imports.own.will_go_to_start.x.lower() == "john_the_ripper": # john_the_ripper (+)

        try:

            print("\n")
            os.system(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\john_the_ripper\\run\\john.exe"))
            #print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"] + "\\imports\\own\\imports\\mimikatz-master\\mimikatz-master\\x64\\mimikatz.exe"))
            imports.own.will_go_to_start.main()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "morse_code": # morse_code (+)

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

            try:

                #defret = input(Fore.YELLOW + "\nEnter site name with (.com): " + Fore.WHITE)
                get_ip_site_start(defret76)

            except:

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
            
    if imports.own.will_go_to_start.x.lower() == "stealer": # stealer (+)

        try:
            try:
                is_admin = os.getuid() == 0
            except AttributeError:
                is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

            if is_admin == False:
                
                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Run console as admin!)" + Fore.WHITE)
                imports.own.will_go_to_start.main()

            elif is_admin == True:

                print(" ")
                os.system("start " + os.path.join(os.environ["OXDAN-DRAGON-PYTHON"] + "\imports\own\imports\importnt_folder\start_2.bat"));
                print("Copying files was " + Fore.GREEN + "successfully" + Fore.WHITE + " finished in Oxdan-Dragon-Python dir.")
                imports.own.will_go_to_start.main()
            
        except:

            imports.own.will_go_to_start.main()
            
    if imports.own.will_go_to_start.x.lower() == "phone_search": # phone_search (+)

        try:

            #ip_search()
            # taking input the phonenumber along with the country code
            print(" ")
            print(Fore.RED + "Write 'esc' (for exit)")
            number = input(Fore.YELLOW + "Enter Phone Number with country code like (+14129089359): ")

            print(Fore.WHITE)

            if number == "esc":
    
                imports.own.will_go_to_start.main()

            # Parsing the phonenumber string to convert it into phonenumber format
            phoneNumber = phonenumbers.parse(number)
 
            # Storing the API Key in the Key variable
            Key = "4ce6fc5fb55a4e0883a37f1513389bf2" #generate your api https://opencagedata.com/api
 
            # Using the geocoder module of phonenumbers to print the Location in console
            yourLocation = geocoder.description_for_number(phoneNumber,"en")
            region = yourLocation
            country = pycountry.countries.get(alpha_2 = region_code_for_number(phoneNumber))
            city = "test"
            zip_cor = "test"
            not_sure = "(No info)"

            print(" ") 
            print("Country: " + country.name)
            sleep(0.01)
            print("Region: " + region)
            sleep(0.01)
            print("City: " + not_sure)
            sleep(0.01)
            print("Zip: " + not_sure)
            sleep(0.01)
            print("Y: " + not_sure)
            sleep(0.01)
            print("X: " + not_sure)
            sleep(0.01)
            #print(" ")
            imports.own.will_go_to_start.main()

        except:

            print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter Phone number with country code!)" + Fore.WHITE)
            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "wifi_hack": # wifi_hack (+)

        try:

            wifi_hack_start()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "inject_prog": # inject_prog (+)

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

            try:

                    if name_uy == "w" or name_uy == "W": # pas gen w (+)
            
                        try:

                            pas_gen_w_start()

                        except:

                            imports.own.will_go_to_start.main()

                    if name_uy == "u" or name_uy == "U": # pas gen u (+) 
            
                        try:

                            pas_gen_u_start()

                        except:

                            imports.own.will_go_to_start.main()

                    if name_uy == "n" or name_uy == "N": # pas gen n (+) 
            
                        try:

                            pas_gen_n_start()

                        except:

                            imports.own.will_go_to_start.main()

                    if name_uy == "nw" or name_uy == "NW": # pas gen nw (+) 
            
                        try:

                            pas_gen_nw_start()

                        except:

                            imports.own.will_go_to_start.main()

            except:

                    tokens = imports.own.will_go_to_start.writex.split(" ")
                    name = tokens[1]

                    if name == "w" or name == "W": # pas gen w (+)
            
                        try:

                            pas_gen_w_start()

                        except:

                            imports.own.will_go_to_start.main()

                    if name == "u" or name == "U": # pas gen u (+) 
            
                        try:

                            pas_gen_u_start()

                        except:

                            imports.own.will_go_to_start.main()

                    if name == "n" or name == "N": # pas gen n (+) 
            
                        try:

                            pas_gen_n_start()

                        except:

                            imports.own.will_go_to_start.main()

                    if name == "nw" or name == "NW": # pas gen nw (+) 
            
                        try:

                            pas_gen_nw_start()

                        except:

                            imports.own.will_go_to_start.main()

        except:
                    
                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter pas gen option!)\n" + Fore.WHITE)
                    getch()
                    imports.own.will_go_to_start.main()