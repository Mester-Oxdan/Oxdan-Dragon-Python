from msvcrt import getch
import imports.own.will_go_to_start
import ctypes
from colorama import Fore
import time
import sys 
import win32console
import socket
import shutil
import os
import requests
import imports.own.start_start
import imports.own.instructions
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from imports.own.i_start import i_start
from imports.own.color_start import color_start
from imports.own.color_back_start import color_back_start
from imports.own.main_start_start import main_start_start
from imports.own.size_start import size_start
from imports.own.system_info_start import system_info_start
from imports.own.my_location_start import my_location_start
from imports.own.energy_start import energy_start
from imports.own.send_ph_message_start import send_ph_message_start
from imports.own.my_volume_level23 import my_volume_level
from imports.own.commands_start import commands_start
from imports.own.tips_start import tips_start
from imports.own.links_start import links_start
from imports.own.dragon_helper_start import dragon_helper_start
from imports.own.helpers_start import helpers_start
from imports.own.donators_start import donators_start
from imports.own.set_volume_level_start import set_volume_level_start

def Own():
    

    imports.own.will_go_to_start.which1 

    if imports.own.will_go_to_start.x.lower() == "i?": # i? (+)
            
            try:

                i_start()

            except:

                imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "color": # color (+)
            
            try:

                color_start()

            except:

                imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "color_back": # colorback (+)
            
            try:

                color_back_start()

            except:

                imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "shutdown": # shutdown (+)
            
            try:

                os.system("shutdown /s")

            except:

                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "restart": # restart (+)

            try:

                os.system("shutdown /r")

            except:

                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "&main": # &main (+)
            
            try:

                main_start_start()

            except:

                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "donators": # donators (+)
            
            try:

                donators_start()

            except:

                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "helpers": # helpers (+)
            
            try:

                helpers_start()

            except:

                imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "size": # size (+)

            try:

                size_start()

            except:

                imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "data": # data (+)

            try:

                print("\n" + time.ctime())
                imports.own.will_go_to_start.main()

            except:

                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "administrator" or imports.own.will_go_to_start.x.lower() == "admin" or imports.own.will_go_to_start.x.lower() == "superuser": # admininistrator (+)

         # (+)
         try:

                path = os.getcwd()
                #os.chdir("..")

                #os.system("start " + path + "\CONSOLE_OXDAN_DRAGON_PYTHON.py")

                # Перезапускаем скрипт с правами админа
                ctypes.windll.shell32.ShellExecuteW( None, "runas", sys.executable, os.path.join(os.environ["OXDAN-DRAGON-PYTHON"] + "\CONSOLE_OXDAN_DRAGON_PYTHON.py"), None, 1)
                exit(0)  # выходим из старой версии скрипта
                #will_go_to_start.main()

         except:

             imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "title": # title (+)

                try:
                    
                    try:

                        win32console.SetConsoleTitle(a_tit)
                        imports.own.will_go_to_start.main()

                    except:

                        tokens = imports.own.will_go_to_start.writex.split(" ")
                        a = tokens[1]
                        win32console.SetConsoleTitle(a)
                        imports.own.will_go_to_start.main()

                except:

                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter name for title!)" + Fore.WHITE + "\n")
                    imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "system_info": # system_info (+)

            try:

                system_info_start()

            except:

                imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "send_ph_message": # send_ph_message (+)

        try:

            send_ph_message_start()

        except:

            imports.own.will_go_to_start.main()
            
    if imports.own.will_go_to_start.x.lower() == "donate": # donate (+)

        try:
           
           line_y1 = 0

           os.system("cls");
           #print("                                     ");
           while line_y1 != 4:
                print("                                     ")
                line_y1 += 1
           
           print("                                     Thanks for wanting to send money but if you");
           print("                                    haven't changed your mind, here the author's")
           print("                                  card number, don't exceed the amount ($1 - $200).")
           print("                                                       Thanks.")
           print(" ")
           print("                                           \033[0;33mCard number:\033[0;37m 4403 9352 3234 1307")
           print(" ")
           print("                                              Press any key to go back.")
           getch()
           print(" ")
           imports.own.will_go_to_start.main()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "rules": # rules (+)

        try:

           imports.own.instructions.instructions_rules()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "commands": # commands (+)

        try:

           commands_start()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "tips": # tips (+)

        try:

           tips_start()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "links": # links (+)

        try:

           links_start()

        except:

            imports.own.ill_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "dragon_helper": # dragon_helper (+)

        try:

           dragon_helper_start()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "history": # history (+)

        try:
            input_list = imports.own.will_go_to_start.input_list  # Assuming you have a list called input_list

            print(" ")
            for num, item in enumerate(input_list, 1):
                print(str(num) + ") " + item)

            #print(" ")

            imports.own.will_go_to_start.main()

        except:

            imports.own.will_go_to_start.main()

    if imports.own.will_go_to_start.x.lower() == "cls_history": # cls_history (+)

        try:

            #print(" ")

            imports.own.will_go_to_start.input_list = []

            imports.own.will_go_to_start.main()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "my_volume_level": # my_volume_level (+)

            try:

                my_volume_level()

            except:

                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "set_mute": # set_mute (+)

            try:

                try:

                  devices = AudioUtilities.GetSpeakers()
                  interface = devices.Activate(
                                   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                  volume = cast(interface, POINTER(IAudioEndpointVolume))
 
                  # Control volume
                  ##volume.SetMasterVolumeLevel(-0.0, None) #max
                  ##volume.SetMasterVolumeLevel(-5.0, None) #72%

                  if a_tit_2788 == "on":

                        volume.SetMute(0, None)
                        imports.own.will_go_to_start.main()

                  if a_tit_2788 == "off":

                        volume.SetMute(1, None)
                        imports.own.will_go_to_start.main()

                  else:

                      print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter set_mute option!)" + Fore.WHITE)
                      imports.own.will_go_to_start.main()

                except:

                  tokens = imports.own.will_go_to_start.writex.split(" ")
                  a = tokens[1]

                  devices = AudioUtilities.GetSpeakers()
                  interface = devices.Activate(
                                   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                  volume = cast(interface, POINTER(IAudioEndpointVolume))
 
                  # Control volume
                  ##volume.SetMasterVolumeLevel(-0.0, None) #max
                  ##volume.SetMasterVolumeLevel(-5.0, None) #72%

                  if a == "on":

                        volume.SetMute(0, None)
                        imports.own.will_go_to_start.main()

                  if a == "off":

                        volume.SetMute(1, None)
                        imports.own.will_go_to_start.main()

                  else:

                      print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter set_mute option!)" + Fore.WHITE)
                      imports.own.will_go_to_start.main()
                  

            except:

                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter set_mute option!)" + Fore.WHITE)
                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "ip": # ip (+)
            
            try:

                def search_net(ip='127.0.0.1'):

                    response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
                    print(Fore.YELLOW + "Network Ip Address: " + Fore.WHITE + response.get('query'))
                
                hostname=socket.gethostname()
                IPAddr=socket.gethostbyname(hostname)

                response = requests.get('https://api64.ipify.org?format=json').json()
                ip = response["ip"]

                print(Fore.YELLOW + "\nIPv4 Address: " + Fore.WHITE + IPAddr)
                
                search_net(ip = ip)

                imports.own.will_go_to_start.main()

            except:

                imports.own.will_go_to_start.main()
            
    elif imports.own.will_go_to_start.x.lower() == "my_location": # my_location (+)

            try:

                my_location_start()

            except:

                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "set_volume_level": # set_volume_level (+)

            try:
                try:

                    set_volume_level_start(a_iuy)

                except:

                    tokens = imports.own.will_go_to_start.writex.split(" ")
                    a = tokens[1]

                    set_volume_level_start(a)

            except:

                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter integers only!)" + Fore.WHITE)
                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "new" or imports.own.will_go_to_start.x.lower() == "start": # new (+)

            try:

                #path = os.getcwd()
                #os.chdir("..")

                os.system("start " + os.path.join(os.environ["OXDAN-DRAGON-PYTHON"] + "\CONSOLE_OXDAN_DRAGON_PYTHON.py"))

                #os.system(r"start C:\Users\bogda\source\repos\CONSOLE-OXDAN-DRAGON-PYTHON\CONSOLE-OXDAN-DRAGON-PYTHON\CONSOLE_OXDAN_DRAGON_PYTHON.py")
                imports.own.will_go_to_start.main()

            except:

                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "energy" or imports.own.will_go_to_start.x.lower() == "power": # energy (+)
            
            try:

                energy_start()
                
            except:

                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "i_am_here":

        try:

            print("\n\033[0;33mTime spent: \033[0;37m %s seconds, %s minutes, %s hours, %s days" % (round(time.time() - imports.own.start_start.start_time), round((time.time() - start_start.start_time)/60), round(((time.time() - start_start.start_time)/60)/60), round((((time.time() - start_start.start_time)/60)/60)/24)))
            imports.own.will_go_to_start.main()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "memory": # memory (+)

            try:

                total, used, free = shutil.disk_usage("/")

                print(Fore.YELLOW + "\nTotal space: " + Fore.WHITE + "%d GB"  % (total // (2**30)) )
                print(Fore.GREEN + "Free space: " + Fore.WHITE + "%d GB"  % (free // (2**30)) )
                print(Fore.RED + "Used space: " + Fore.WHITE + "%d GB"  % (used // (2**30)) )
                
                imports.own.will_go_to_start.main()

            except:

                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "open": # open (+)

            try:

                try:

                        os.system(r"start " + a_tit_1)

                        imports.own.will_go_to_start.main()

                except:

                        tokens = imports.own.will_go_to_start.writex.split(" ")
                        keyt = tokens[1]

                        os.system(r"start " + keyt)

                        imports.own.will_go_to_start.main()

            except:

                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter path to program!)\n" + Fore.WHITE)
                    #getch()
                    imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "chan_backg": # chan_backg (+)

            try:

                try:

                    tokens = imports.own.will_go_to_start.writex.split(" ")
                    path = tokens[1]
                    ctypes.windll.user32.SystemParametersInfoW(20, 0, str(path) , 0)
                    imports.own.will_go_to_start.main()

                except:

                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter path to photo!)\n" + Fore.WHITE)
                    #getch()
                    imports.own.will_go_to_start.main()

            except:

                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter path to photo!)\n" + Fore.WHITE)
                    #getch()
                    imports.own.will_go_to_start.main()
