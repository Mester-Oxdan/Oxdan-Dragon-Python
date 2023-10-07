from msvcrt import getch
import imports.own.will_go_to_start
from colorama import Fore
import colorama
import ctypes
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