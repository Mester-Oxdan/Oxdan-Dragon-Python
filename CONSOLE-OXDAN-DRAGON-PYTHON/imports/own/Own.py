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
import psutil
from pydub import AudioSegment
from pydub.playback import play
from decimal import Decimal, ROUND_UP, ROUND_HALF_UP

def Own():
    

    imports.own.will_go_to_start.which1 

    if imports.own.will_go_to_start.x.lower() == "i?": # i? (+)
            
            try:

                i_start()

            except:

                imports.own.will_go_to_start.main()

    '''if imports.own.will_go_to_start.x.lower() == "color": # color (+)
            
            try:

                color_start()

            except:

                imports.own.will_go_to_start.main()'''

    if imports.own.will_go_to_start.x.lower() == "color_back": # colorback (+)
            
            try:

                color_back_start()

            except:

                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter color_back option!)" + Fore.WHITE)
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

    if imports.own.will_go_to_start.x.lower() == "date": # date (+)

            try:

                print("\n" + Fore.YELLOW + "Date: " + Fore.WHITE + time.ctime())
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
                ctypes.windll.shell32.ShellExecuteW( None, "runas", sys.executable, path + "\CONSOLE_OXDAN_DRAGON_PYTHON.py", None, 1)
                exit(0)  # выходим из старой версии скрипта
                #will_go_to_start.main()

         except:

             imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "title": # title (+)

                try:

                        tokens = imports.own.will_go_to_start.writex.split(" ")
                        a = tokens[1]
                        win32console.SetConsoleTitle(a)
                        imports.own.will_go_to_start.main()

                except:

                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter name for title!)" + Fore.WHITE + "\n")
                    imports.own.will_go_to_start.main()
                    
    elif imports.own.will_go_to_start.x.lower() == "promo_code": # promo_code (+)

                try:
                    
                    #try:

                        #win32console.SetConsoleTitle(a_tit)
                        #imports.own.will_go_to_start.main()

                    #except:

                        tokens = imports.own.will_go_to_start.writex.split(" ")
                        a = tokens[1]
                        #win32console.SetConsoleTitle(a)
                        if a.lower() == "sans-battle" or a.lower() == "sansbattle" or a.lower() == "sans_battle":
                            
                            print(" ")
                            print(Fore.YELLOW + "Secret Link:" + Fore.WHITE + " https://jcw87.github.io/c2-sans-fight/")
                            #print(" ")
                            imports.own.will_go_to_start.main()
                        if a.lower() == "toby-fox" or a.lower() == "tobyfox" or a.lower() == "toby_fox":
                            
                            print(" ")
                            print("Thanks a lot! You are the hero of my childhood. \n(Big a fan) Thanks for " + Fore.RED + "Undertale" + Fore.WHITE + " game :)")
                            #print(" ")
                            # Load the MP3 audio file
                            audio_file = AudioSegment.from_mp3(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],'imports/own/resources/music/undertale.mp3'))

                            # Play the audio file
                            play(audio_file)
                            imports.own.will_go_to_start.main()
                        if a.lower() == "scott-cawthon" or a.lower() == "scottcawthon" or a.lower() == "scott_cawthon":
                            
                            print(" ")
                            print("Thanks a lot! You are the one more hero of my childhood. \n(Big a fan) Thanks for " + Fore.YELLOW + "Five Nights at Freddy's" + Fore.WHITE + " game :)")
                            #print(" ")
                            # Load the MP3 audio file
                            audio_file = AudioSegment.from_mp3(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],'imports/own/resources/music/freddy_nouse.wav'))

                            # Play the audio file
                            play(audio_file)
                            # Load the MP3 audio file
                            audio_file = AudioSegment.from_mp3(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],'imports/own/resources/music/fnaf_beatbox_1.wav'))

                            # Play the audio file
                            play(audio_file)
                            imports.own.will_go_to_start.main()
                            
                        else:
                            
                            print(" ")
                            print("'" + a + "'" + " Is " + Fore.RED + "wrong" + Fore.WHITE + " promo-code")
                            #print(" ")
                            imports.own.will_go_to_start.main()

                except:

                    print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter promo code name!)" + Fore.WHITE)
                    imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "system_info": # system_info (+)

            try:

                system_info_start()

            except:

                imports.own.will_go_to_start.main()

    """if imports.own.will_go_to_start.x.lower() == "send_ph_message": # send_ph_message (+)

        try:

            send_ph_message_start()

        except:

            imports.own.will_go_to_start.main()"""
            
    if imports.own.will_go_to_start.x.lower() == "donate": # donate (+)

        try:
           
           line_y1 = 0

           os.system("cls");
           #print("                                     ");
           while line_y1 != 4:
                print("                                     ")
                line_y1 += 1
           
           print("                                     Thanks for your support! If you haven't changed your");
           print("                                     mind, here is author's Buy Me A Coffee and Cash App.")
           print("                                        Please don't exceed limit amount ($1 - $100).")
           print("                                                           Thanks.")
           print(" ")
           print("                                                \033[0;33mCash App:\033[0;37m 4403 9352 3234 1307")
           print(" ")
           print("                                     \033[0;33mBuy Me A Coffee:\033[0;37m https://www.buymeacoffee.com/oxdan")
           print(" ")
           print("                                                  Press any key to go back.")
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

    '''if imports.own.will_go_to_start.x.lower() == "dragon_helper": # dragon_helper (+)

        try:

           dragon_helper_start()

        except:

            imports.own.will_go_to_start.main()'''

    if imports.own.will_go_to_start.x.lower() == "history": # history (+)

        try:
            input_list = imports.own.will_go_to_start.input_list  # Assuming you have a list called input_list

            print(" ")
            print(Fore.YELLOW + "HISTORY: " + Fore.WHITE)
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

                  tokens = imports.own.will_go_to_start.writex.split(" ")
                  a = tokens[1]

                  devices = AudioUtilities.GetSpeakers()
                  interface = devices.Activate(
                                   IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
                  volume = cast(interface, POINTER(IAudioEndpointVolume))
 
                  # Control volume
                  ##volume.SetMasterVolumeLevel(-0.0, None) #max
                  ##volume.SetMasterVolumeLevel(-5.0, None) #72%

                  if a == "off":

                        volume.SetMute(0, None)
                        imports.own.will_go_to_start.main()

                  if a == "on":

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

                    tokens = imports.own.will_go_to_start.writex.split(" ")
                    a = tokens[1]

                    set_volume_level_start(a)

            except:

                print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Enter integers only!)" + Fore.WHITE)
                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "new" or imports.own.will_go_to_start.x.lower() == "start": # new (+)

            try:

                path = os.getcwd()
                #os.chdir("..")

                os.system("start " + os.environ["OXDAN-DRAGON-PYTHON"] + "\CONSOLE_OXDAN_DRAGON_PYTHON.py")

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

            print("\n\033[0;33mTime spent: \033[0;37m %s seconds, %s minutes, %s hours, %s days" % (round(time.time() - imports.own.start_start.start_time), round((time.time() - imports.own.start_start.start_time)/60), round(((time.time() - imports.own.start_start.start_time)/60)/60), round((((time.time() - imports.own.start_start.start_time)/60)/60)/24)))
            imports.own.will_go_to_start.main()

        except:

            imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "memory": # memory (+)

            try:

                # Function to get disk type
                def get_disk_type(drive):
                    drive_type = ctypes.windll.kernel32.GetDriveTypeW(drive)
                    types = {
                        0: "UNKNOWN",
                        1: "NO ROOT DIR",
                        2: "REMOVABLE",
                        3: "FIXED",
                        4: "REMOTE",
                        5: "CDROM",
                        6: "RAMDISK"
                    }
                    return types.get(drive_type, "UNKNOWN")
                    #print(Fore.RED + "\n(!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Unknown disk type!)\n" + Fore.WHITE)

                # Get disk usage information
                total, used, free = shutil.disk_usage("/")

                # Get disk partition and file system information
                partitions = psutil.disk_partitions()
                disk_info = {}
                for partition in partitions:
                    usage = psutil.disk_usage(partition.mountpoint)
                    disk_type = get_disk_type(partition.device + '\\')
                    disk_info[partition.device] = {
                        'file_system': partition.fstype,
                        'total': usage.total // (2**30), #(usage.total // (2**30)).quantize(Decimal('0.001'), ROUND_HALF_UP),
                        'used': usage.used // (2**30),
                        'free': usage.free // (2**30),
                        'type': disk_type
                    }

                # Print disk usage information
                #print(" ")    
                for device, info in disk_info.items():
                    print(Fore.YELLOW + f"\nDisk Device: {device}")
                    print(Fore.YELLOW + "Total space: " + Fore.WHITE + "%d GB" % info['total'])
                    print(Fore.GREEN + "Free space: " + Fore.WHITE + "%d GB" % info['free'])
                    print(Fore.RED + "Used space: " + Fore.WHITE + "%d GB" % info['used'])
                    print(Fore.MAGENTA + "Disk type: " + Fore.WHITE + info['type'])
                    print(Fore.CYAN + "File system: " + Fore.WHITE + info['file_system'])
                    
                
                imports.own.will_go_to_start.main()

            except:

                imports.own.will_go_to_start.main()

    elif imports.own.will_go_to_start.x.lower() == "open": # open (+)

            try:

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
