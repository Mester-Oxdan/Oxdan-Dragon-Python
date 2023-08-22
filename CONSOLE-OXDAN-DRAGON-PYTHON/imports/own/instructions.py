from time import sleep
from msvcrt import getch
import os
import imports.own.start_start
import imports.own.will_go_to_start
from colorama import Fore

def instructions():

    os.system("cls")
    print(" ")
    sleep(0.01)
    print(" ")
    sleep(0.01)
    print(Fore.RED + "                                                           !RULES!" + Fore.WHITE)
    sleep(0.01)
    print(" ")
    sleep(0.01)
    print("   First command which you need to know it is " + Fore.YELLOW + "-h" + Fore.WHITE + ", this command will print all commands which this console have.")
    sleep(0.01)
    print(" ")
    sleep(0.01)
    print(Fore.RED + "   !" + Fore.YELLOW + "Remember" + Fore.WHITE + ", Author (OXDAN) do not care and do not responsible for what you doing.")
    sleep(0.01)
    print(" ")
    sleep(0.01)
    print("   This console intended for learning programing and how it is working, you can see code of this console on (https://github.com/Mester-Oxdan) Author (OXDAN) github.")
    sleep(0.01)
    print(" ")
    sleep(0.01)
    print(Fore.RED + "                                            Press any key to go in the main menu." + Fore.WHITE)
    sleep(0.01)
    getch()
    imports.own.start_start.start_start()

def instructions_rules():

    os.system("cls")
    print(" ")
    sleep(0.01)
    print(" ")
    sleep(0.01)
    print(Fore.RED + "                                                           !RULES!" + Fore.WHITE)
    sleep(0.01)
    print(" ")
    sleep(0.01)
    print("   First command which you need to know it is " + Fore.YELLOW + "-h" + Fore.WHITE + ", this command will print all commands which this console have.")
    sleep(0.01)
    print(" ")
    sleep(0.01)
    print(Fore.RED + "   !" + Fore.YELLOW + "Remember" + Fore.WHITE + ", Author (OXDAN) do not care and do not responsible for what you doing.")
    sleep(0.01)
    print(" ")
    sleep(0.01)
    print("   This console intended for learning programing and how it is working, you can see code of this console on (https://github.com/Mester-Oxdan) Author (OXDAN) github.")
    sleep(0.01)
    print(" ")
    sleep(0.01)
    print(Fore.RED + "                                            Press any key to go back." + Fore.WHITE)
    sleep(0.01)
    getch()
    imports.own.will_go_to_start.main()
