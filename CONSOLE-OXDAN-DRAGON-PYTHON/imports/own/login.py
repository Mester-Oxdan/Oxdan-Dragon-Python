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

def login():

    os.system("cls")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print("                                                              ")
    print(colorama.Fore.RED + "                                                          Enter 'esc' (for exit)")
    print(colorama.Fore.RED + "                                                               LOGIN:" + colorama.Fore.WHITE)
    email = input(colorama.Fore.YELLOW + "\n                                                              USERNAME: " + colorama.Fore.RED)

    if imports.own.will_go_to_start.remove_098(email.lower()) == "esc":

        imports.own.start_start.start_start()

    pwd = input(colorama.Fore.YELLOW + "                                                              PASSWORD: " + colorama.Fore.RED)
    
    if imports.own.will_go_to_start.remove_098(pwd.lower()) == "esc":

        imports.own.start_start.start_start()

    print(colorama.Fore.WHITE)

    auth = pwd.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    found_password = False
    
    #try:

    with builtins.open(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/login_data_base.txt"), "r") as f:
        
            for line in f:

                  tokens = line.split(" ")

                  if (len(tokens) < 2 ):

                      continue

                  stored_email = tokens[0].strip()
                  stored_pwd = tokens[1].strip()

                  if auth_hash == stored_pwd and email != stored_email:

                     print(colorama.Fore.RED + "                                                         (!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Wrong username!)\n" + colorama.Fore.WHITE)
                     msvcrt.getch()
                     imports.own.start_start.start_start()

                  elif email == stored_email and auth_hash != stored_pwd:

                     found_password = True
                     print(colorama.Fore.RED + "                                                         (!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Wrong password!)\n" + colorama.Fore.WHITE)
                     msvcrt.getch()
                     imports.own.start_start.start_start()

                  elif email == stored_email and auth_hash == stored_pwd:
                     
                         found_password = True
                         os.system("cls")
                         print(colorama.Fore.YELLOW + "Oxdan" + colorama.Fore.RED + " Dragon" + colorama.Fore.WHITE + " [ Version: 2.2024 [ENGLISH] (PYTHON) [WINDOWS] ] ") # intro cmd (+)
                         time.sleep(0.01)
                         print("(p) Oxdan Praduction. ")
                         time.sleep(0.01)
                         imports.own.will_go_to_start.main()
                    
                  else:

                    continue

            if found_password == False:

                     print(colorama.Fore.RED + "\n                                                         (!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Account did not found!)\n" + colorama.Fore.WHITE)
                     msvcrt.getch()
                     imports.own.start_start.start_start()

    #except:

        #if imports.own.will_go_to_start.x == "prank_button" or imports.own.will_go_to_start.x == "exit" or imports.own.will_go_to_start.x == "esc" or imports.own.will_go_to_start.x == "quit" or imports.own.will_go_to_start.x == "admin" or imports.own.will_go_to_start.x == "administrator" or imports.own.will_go_to_start.x == "superuser":

                #quit(0)

        #if imports.own.will_go_to_start.x == "author":

            

            #imports.own.will_go_to_start.main()

        #else:

                 #print(colorama.Fore.RED + "\n                                                         (!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Account did not found!)\n" + colorama.Fore.WHITE)
                 #msvcrt.getch()
                 #imports.own.start_start.start_start()
