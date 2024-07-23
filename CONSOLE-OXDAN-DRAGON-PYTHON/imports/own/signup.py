import msvcrt
import os
from colorama import Fore
import builtins
import hashlib
import imports.own.start_start
import imports.own.will_go_to_start

def signup():

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
    print(Fore.RED + "                                                          Enter 'esc' (for exit)")
    print(Fore.RED + "                                                             REGISTRATION:" + Fore.WHITE)
    #print(" ")
    email = input(Fore.YELLOW + "\n                                                              USERNAME: " + Fore.RED)

    if imports.own.will_go_to_start.remove_098(email.lower()) == "esc":

        imports.own.start_start.start_start()

    pwd = input(Fore.YELLOW + "                                                              PASSWORD: " + Fore.RED)

    if imports.own.will_go_to_start.remove_098(pwd.lower()) == "esc":

        imports.own.start_start.start_start()

    enc = pwd.encode()
    hash1 = hashlib.md5(enc).hexdigest()
    checkpas = False

    try:

        if checkpas == False:
            with builtins.open("imports/own/login_data_base.txt", "r") as f:

                    for line in f:
                         tokens = line.split(" ")
                         if (len(tokens) < 2 ):
                            continue

                         stored_email = tokens[0].strip()
                         stored_pwd = tokens[1].strip()

                         if email == stored_email:

                            checkpas == True
                            print(Fore.RED + "\n                                                         (!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Username already exist!)\n" + Fore.WHITE)
                            msvcrt.getch()
                            imports.own.start_start.start_start()

                         if hash1 == stored_pwd:

                            checkpas == True
                            print(Fore.RED + "\n                                                         (!ERROR!) " + Fore.WHITE + "=" + Fore.GREEN + " (!Password already exist!)\n" + Fore.WHITE)
                            msvcrt.getch()
                            imports.own.start_start.start_start()
                     
                         else:
                             continue

                    if hash1 != stored_pwd and email != stored_email:
                            
                                checkpas == True
                                with builtins.open("imports/own/login_data_base.txt", "a") as fa:

                                    fa.write(email + " " + hash1 + "\n")

                                print(Fore.GREEN + "\n                                                         !REGISTRATION SUCCESSFUL!") # registered successfully!
                                print(Fore.YELLOW)
                                msvcrt.getch()
                                imports.own.start_start.start_start()

    except:

                                checkpas == True
                                with builtins.open("imports/own/login_data_base.txt", "a") as fa:

                                    fa.write(email + " " + hash1 + "\n")

                                print(Fore.GREEN + "\n                                                         !REGISTRATION SUCCESSFUL!") # registered successfully!
                                print(Fore.YELLOW)
                                msvcrt.getch()
                                imports.own.start_start.start_start()
