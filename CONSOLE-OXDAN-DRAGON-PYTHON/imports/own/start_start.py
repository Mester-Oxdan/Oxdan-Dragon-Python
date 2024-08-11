import os

try:
    import colorama
    import keyboard
    import ctypes
    import git
    import requests
    import shutil
    import time
    import winotify 
    import subprocess
    import builtins
    import pygame
except ImportError:

        os.system("pip install colorama")
        os.system("pip install keyboard")
        os.system("pip install ctypes")
        os.system("pip install git")
        os.system("pip install requests")
        os.system("pip install shutil")
        os.system("pip install winotify")
        os.system("pip install subprocess")
        os.system("pip install builtins")
        os.system("pip install pygame")

import msvcrt
import os
import colorama
import keyboard
import imports.own.login
import imports.own.signup
import imports.own.instructions
import ctypes
import time
import git
import requests
import shutil
import time

start_time = time.time()

def printMenu(items, active_index):

    print(" ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    #print("                                                              ")
    for index, item in enumerate(items):
        if index == active_index:
            #print(f'\033[31;47m{item}\033[0m')

            print(colorama.Fore.RED + f'{item}' + colorama.Fore.YELLOW)
        else:
            print(item)

def start_start():

    print(colorama.Fore.YELLOW)
    os.system("cls")
    #print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/resources/music/steel.ogg"))
    #print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"], "resources\math_game\kenvector_future.ttf"))
    #print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/config.txt"))
    #print(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/my_dragon_ico.jpg"))
    #msvcrt.getch()

    Menu = ["                                                              REGISTRATION", "                                                              LOGIN", "                                                              SKIP", "                                                              INSTRUCTIONS", "                                                              EXIT"]
    active_menu = 0
    keyboard.press(72)

    while True:

        key = ord(msvcrt.getch())

        if key == 27:
            
            exit(0)

        elif key == 72:

            if active_menu > 0:
                active_menu -= 1
            os.system("cls")
            
                
            #break

        elif key == 80:

            if active_menu < 4:
                active_menu += 1
            os.system("cls")

            #break

        elif key == 13:

            if active_menu == 0: # 1

                os.system("cls")
                imports.own.signup.signup()

            if active_menu == 1: # 2

                os.system("cls")
                imports.own.login.login()

            if active_menu == 2: # 3

                os.system("cls")
                print(colorama.Fore.YELLOW + "Oxdan" + colorama.Fore.RED + " Dragon" + colorama.Fore.WHITE + " [ Version: 2.2024 [ENGLISH] (PYTHON) [WINDOWS] ] ") # intro cmd (+)
                time.sleep(0.01)
                print("(p) Oxdan Praduction. ")
                time.sleep(0.01)
                imports.own.will_go_to_start.main()
                
            if active_menu == 3: # 4

                os.system("cls")
                imports.own.instructions.instructions()

            if active_menu == 4: # 5

                #os.system("cls")
                exit(0)

        elif key == 49: # 1

                os.system("cls")
                imports.own.signup.signup()

        elif key == 50: # 2

                os.system("cls")
                imports.own.login.login()
                
        elif key == 51: # 3

                os.system("cls")
                print(colorama.Fore.YELLOW + "Oxdan" + colorama.Fore.RED + " Dragon" + colorama.Fore.WHITE + " [ Version: 2.2024 [ENGLISH] (PYTHON) [WINDOWS] ] ") # intro cmd (+)
                time.sleep(0.01)
                print("(p) Oxdan Praduction. ")
                time.sleep(0.01)
                imports.own.will_go_to_start.main()

        elif key == 52: # 4

                os.system("cls")
                imports.own.instructions.instructions()

        elif key == 53: # 5

                os.system("cls")
                exit(0)
            
        else:

            continue

        printMenu(Menu, active_menu)
