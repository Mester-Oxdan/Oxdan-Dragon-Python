import msvcrt
import os
import time
import colorama
import builtins
import hashlib
import sys 
import imports.own.start_start
import imports.own.will_go_to_start
import imports.own.Pranks
import pyglet
from colorama import Fore

def my_accounts_start():

    found_password = False
    
    #try:
    print(" ")
    print(Fore.RED + "     YOUR ACCOUNTS: " + Fore.WHITE)
    print(Fore.YELLOW + "USERNAME:      PASSWORD:" + Fore.WHITE)
    with builtins.open(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/login_data_base.txt"), "r") as f:
        
            for line in f:

                  tokens = line.split(" ")

                  if (len(tokens) < 2 ):

                      continue

                  stored_email = tokens[0].strip()
                  stored_pwd = tokens[1].strip()

                  print("    " + stored_email + "          " + "    " + stored_pwd)

                  continue
            
    imports.own.will_go_to_start.main()
