from msvcrt import getch
import os
from colorama import Fore

def update():
    
    os.system("git pull")
    print(" ")
    print("Program updated " + Fore.GREEN + "successfully." + Fore.WHITE + " Please close this file and start your program again.")
    getch()

update()