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
    print(colorama.Fore.RED + "                                                          Write 'esc' (for exit)")
    print(colorama.Fore.RED + "                                                               LOGIN:" + colorama.Fore.WHITE)
    email = input(colorama.Fore.YELLOW + "\n                                                              USERNAME: " + colorama.Fore.RED)

    if email == "esc":

        imports.own.start_start.start_start()

    pwd = input(colorama.Fore.YELLOW + "                                                              PASSWORD: " + colorama.Fore.RED)
    
    if pwd == "esc":

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
                  
                         def ask():

                             try:

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
                                 print(colorama.Fore.GREEN + "\n                                                              !LOGIN SUCCESSFUL!")
                                 print(colorama.Fore.YELLOW)
                                 print("                                                              1) Add email")
                                 print("                                                              2) Add phone number")
                                 print("                                                              3) Skip")
                                 global option
                                 option = int(input(colorama.Fore.YELLOW + "\n                                                              Enter option: " + colorama.Fore.RED))
                         
                             except ValueError:

                                 print(colorama.Fore.RED + "\n                                                         (!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Only integers!)\n" + colorama.Fore.WHITE)
                                 msvcrt.getch()
                                 ask()

                             if option > 3 or option < 1:

                                 print(colorama.Fore.RED + "\n                                                         (!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Out of range!)\n" + colorama.Fore.WHITE)
                                 msvcrt.getch()
                                 ask()

                         ask()

                         while True:

                             if option == 1:
                                        
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
                                         email12 = input(colorama.Fore.YELLOW + "\n                                                              EMAIL: " + colorama.Fore.RED)

                                         encemail = email12.encode()
                                         hash1 = hashlib.md5(encemail).hexdigest()
                                         checkpass1 = False

                                         try:

                                             if checkpass1 == False:

                                                 with builtins.open(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/email_data_base.txt"), "r") as f:
                                                     #f.write(hash1)
                                                     for line in f:

                                                         tokens = line.split(" ")
                                                         if (len(tokens) < 1 ):
                                                             continue

                                                         #stored_email = tokens[0].strip()
                                                         stored_pwd = tokens[0].strip()

                                                         if hash1 == stored_pwd:
                                                            checkpass1 == True
                                                            print(colorama.Fore.RED + "\n                                                         (!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Email already exist!)\n" + colorama.Fore.WHITE)
                                                            msvcrt.getch()
                                                    
                                                            ask()

                                                         else:
                                                              continue
                                     
                                                     if hash1 != stored_pwd:

                                                         with builtins.open(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/email_data_base.txt"), "a") as f:

                                                                f.write(hash1 + "\n")

                                                         print(colorama.Fore.GREEN + "\n                                                           !EMAIL SUCCESSFUL!")
                                                         print(colorama.Fore.WHITE)
                                                         msvcrt.getch()
                                                         ask()

                                         except:

                                                     with builtins.open(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/email_data_base.txt"), "a") as f:

                                                            f.write(hash1 + "\n")

                                                     print(colorama.Fore.GREEN + "\n                                                           !EMAIL SUCCESSFUL!")
                                                     print(colorama.Fore.WHITE)
                                                     msvcrt.getch()
                                                     ask()

                             if option == 2:

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
                                         phonenum = input(colorama.Fore.YELLOW + "\n                                                              PHONE NUMBER: " + colorama.Fore.RED)

                                         encphone = phonenum.encode()
                                         hash1 = hashlib.md5(encphone).hexdigest()
                                         check = False

                                         try:

                                             if check == False:

                                                 with builtins.open(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/phone_number_data_base.txt"), "r") as f:

                                                     #f.write(hash1)
                                                     for line in f:
                                                         tokens = line.split(" ")
                                                         if (len(tokens) < 1 ):
                                                             continue

                                                         #stored_email = tokens[0].strip()
                                                         stored_pwd = tokens[0].strip()

                                                         if hash1 == stored_pwd:
                                                            check == True
                                                            print(colorama.Fore.RED + "\n                                                         (!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Phone number already exist!)\n" + colorama.Fore.WHITE)
                                                            msvcrt.getch()
                                                            ask()

                                                         else:
                                                              continue
                                     
                                                     if hash1 != stored_pwd:

                                                         with builtins.open(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/phone_number_data_base.txt"), "a") as f:

                                                             f.write(hash1 + "\n")

                                                         print(colorama.Fore.GREEN + "\n                                                           !PHONE NUMBER SUCCESSFUL!")
                                                         print(colorama.Fore.WHITE)
                                                         msvcrt.getch()
                                                         ask();

                                         except:

                                                         with builtins.open(os.path.join(os.environ["OXDAN-DRAGON-PYTHON"],"imports/own/phone_number_data_base.txt"), "a") as f:

                                                             f.write(hash1 + "\n")

                                                         print(colorama.Fore.GREEN + "\n                                                           !PHONE NUMBER SUCCESSFUL!")
                                                         print(colorama.Fore.WHITE)
                                                         msvcrt.getch()
                                                         ask();

                             if option == 3:
                                    
                                            if sys.platform == "win32":

                                                            # Windows...
                                                            os.system("cls")
                                                            print(colorama.Fore.YELLOW + "Oxdan" + colorama.Fore.RED + " Dragon" + colorama.Fore.WHITE + " [ Version: 1.2023 [ENGLISH] (PYTHON) [WINDOWS] ] ") # intro cmd (+)
                                                            time.sleep(0.01)
                                                            print("(p) Oxdan Praduction. ")
                                                            time.sleep(0.01)
                                                            imports.own.will_go_to_start.main()

                             if option <= 0 or option > 3:
                                     print(colorama.Fore.RED + "\n                                                         (!ERROR!) " + colorama.Fore.WHITE + "=" + colorama.Fore.GREEN + " (!Enter option!)\n" + colorama.Fore.WHITE)
                                     msvcrt.getch()
                                     ask()
                    
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
