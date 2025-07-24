from msvcrt import getch
import os
import keyboard
from colorama import Fore
import imports.own.will_go_to_start

def ascii_code_start():

            os.system("cls")

            while True:

                os.system('cls')
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(" ")
                print(Fore.RED + "                                                                   Press 'Esc' for exit")
                print(Fore.YELLOW + "                                                                Press any key (ESC == 27)")
                print(Fore.WHITE + " ")
                print("                                                                        " + "code " + str((ord(getch()))))

                getch()

                if keyboard.is_pressed('Esc'):

                    imports.own.will_go_to_start.main()