import pyautogui
import os
import imports.own.will_go_to_start
import keyboard
from colorama import Fore

def cor_desk_start():
                
                os.system("cls")
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
                print(" ")
                print(Fore.RED + "                                                              Press 'esc' (for exit)" + Fore.WHITE)
                
                while True:

                    t, y = pyautogui.position()
                    
                    positionStr = Fore.YELLOW + '                                                             d. X: ' + Fore.WHITE + str(t).rjust(4) + Fore.YELLOW + '  d. Y: ' + Fore.WHITE + str(y).rjust(4)
                    print(positionStr, end='')
                    print('\b' * len(positionStr), end='', flush=True)

                    if keyboard.is_pressed('Esc'):

                        print(" ")
                        imports.own.will_go_to_start.main()
